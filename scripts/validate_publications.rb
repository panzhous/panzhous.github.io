#!/usr/bin/env ruby

require "yaml"
require "nokogiri"

ROOT = File.expand_path("..", __dir__)
SOURCE_PATH = File.join(ROOT, "_pages", "publication.md")
TAXONOMY_PATH = File.join(ROOT, "_data", "publication_taxonomy.yml")

source = File.read(SOURCE_PATH, encoding: "UTF-8")
taxonomy = YAML.safe_load_file(TAXONOMY_PATH)

full_section = source[/##### \*\*Full Publications\*\*(.*?)##### \*\*Books and Patents\*\*/m, 1]
abort "Could not find the Full Publications section" unless full_section

fragment = Nokogiri::HTML.fragment(full_section)
publication_list = fragment.at_css("[data-publication-list]")
abort "Could not find the Full Publications list" unless publication_list

full_publications = publication_list.inner_html

lines = taxonomy.to_h { |line| [line.fetch("id"), line] }
subtopics = taxonomy.flat_map { |line| line.fetch("subtopics") }.to_h { |topic| [topic.fetch("id"), topic] }
errors = []
entries = []
current_year = nil
publication_lines = full_publications.lines
heading_years = []

year_groups = publication_list.xpath("./section[@data-publication-year-group]")
errors << "Expected 11 publication year groups, found #{year_groups.length}" unless year_groups.length == 11
year_groups.each do |group|
  year = group["data-year"]
  heading = group.at_xpath("./h4[@class='publication-year']")
  ordered_list = group.at_xpath("./ol[contains(concat(' ', normalize-space(@class), ' '), ' biblist ')]")
  errors << "Year group #{year.inspect}: missing direct publication heading" unless heading
  errors << "Year group #{year.inspect}: heading id does not match" unless heading&.[]("id") == "publications-#{year}"
  errors << "Year group #{year.inspect}: missing direct ordered list" unless ordered_list
  if ordered_list
    invalid_children = ordered_list.element_children.reject { |child| child.name == "li" }
    errors << "Year group #{year.inspect}: ordered list has non-list-item children" unless invalid_children.empty?
  end
end

full_publications.scan(/<h4([^>]*)>\s*<a name=['"](\d{4})['"]>/m).each do |attribute_text, anchor_year|
  attributes = attribute_text.scan(/([a-z-]+)="([^"]*)"/).to_h
  heading_years << anchor_year
  errors << "Year #{anchor_year}: class must include publication-year" unless attributes.fetch("class", "").split.include?("publication-year")
  errors << "Year #{anchor_year}: data-year #{attributes['data-year'].inspect} does not match its anchor" unless attributes["data-year"] == anchor_year
end

heading_years.tally.select { |_year, count| count > 1 }.each_key do |year|
  errors << "duplicate year heading #{year.inspect}"
end

publication_lines.each_with_index do |line, line_index|
  current_year = Regexp.last_match(1) if line.match(/<a name=['"](\d{4})['"]>/)
  next unless line.include?("<li")

  attributes = line.scan(/([a-z-]+)="([^"]*)"/).to_h
  entries << attributes
  title = publication_lines[line_index..]
    &.join
    &.match(/<strong>(.*?)<\/strong>/m)
    &.captures
    &.first
    &.gsub(/<[^>]+>/, "")
    &.gsub(/\s+/, " ")
    &.strip || "entry near line #{line_index + 1}"

  required = %w[id class data-year data-research-line data-keywords]
  required.each do |attribute|
    errors << "#{title}: missing #{attribute}" if attributes[attribute].to_s.empty?
  end

  errors << "#{title}: class must include publication-item" unless attributes.fetch("class", "").split.include?("publication-item")
  errors << "#{title}: data-year #{attributes['data-year'].inspect} does not match heading #{current_year.inspect}" unless attributes["data-year"] == current_year

  research_line = lines[attributes["data-research-line"]]
  errors << "#{title}: unknown research line #{attributes['data-research-line'].inspect}" unless research_line

  subtopic = attributes["data-subtopic"]
  if attributes["data-research-line"] == "architecture-design"
    errors << "#{title}: Architecture Design must not have data-subtopic" unless subtopic.to_s.empty?
  elsif research_line
    errors << "#{title}: missing data-subtopic" if subtopic.to_s.empty?
    allowed = research_line.fetch("subtopics").map { |topic| topic.fetch("id") }
    errors << "#{title}: #{subtopic.inspect} is not a subtopic of #{research_line.fetch('label')}" unless allowed.include?(subtopic)
  end

  keywords = attributes.fetch("data-keywords", "").split(",").map(&:strip).reject(&:empty?)
  errors << "#{title}: add at least three comma-separated keywords" if keywords.length < 3
end

ids = entries.filter_map { |entry| entry["id"] }
ids.tally.select { |_id, count| count > 1 }.each_key do |id|
  errors << "duplicate publication id #{id.inspect}"
end

entry_years = entries.filter_map { |entry| entry["data-year"] }.uniq
(entry_years - heading_years).each { |year| errors << "missing year heading for #{year}" }

errors << "No publication entries found" if entries.empty?
errors << "No publication year headings found" if heading_years.empty?

unless errors.empty?
  warn errors.map { |error| "ERROR: #{error}" }.join("\n")
  exit 1
end

counts = entries.group_by { |entry| entry.fetch("data-research-line") }.transform_values(&:length)
puts "Validated #{entries.length} full publications."
taxonomy.each do |research_line|
  id = research_line.fetch("id")
  puts "- #{research_line.fetch('label')}: #{counts.fetch(id, 0)}"
  research_line.fetch("subtopics").each do |subtopic|
    count = entries.count { |entry| entry["data-subtopic"] == subtopic.fetch("id") }
    puts "  - #{subtopic.fetch('label')}: #{count}"
  end
end
