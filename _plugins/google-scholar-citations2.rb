require 'open-uri'
require 'nokogiri'

# Replace with an array of your article IDs
# ARTICLE_IDS = ['Article ID 1', 'Article Id 2', 'Article Id 3'].freeze # change to real value
SCHOLAR_ID = '0b7ZqlcAAAAJ'.freeze # change to real value

def fetch_citation_counts(article_ids)
  article_citations = {}

  # Iterate through each article ID
  article_ids.each do |article_id|
    article_url = "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=#{SCHOLAR_ID}&citation_for_view=#{SCHOLAR_ID}:#{article_id}"

    begin
      doc = Nokogiri::HTML(URI.parse(article_url).open)

      # Attempt to extract the "Cited by n" string from the meta tags
      citation_count = 0

      # Look for meta tags with "name" attribute set to "description"
      description_meta = doc.css('meta[name="description"]')
      og_description_meta = doc.css('meta[property="og:description"]')

      if !description_meta.empty?
        cited_by_text = description_meta[0]['content']
        matches = cited_by_text.match(/Cited by (\d+)/)

        if matches
          citation_count = matches[1].to_i
        end
      elsif !og_description_meta.empty?
        cited_by_text = og_description_meta[0]['content']
        matches = cited_by_text.match(/Cited by (\d+)/)

        if matches
          citation_count = matches[1].to_i
        end
      end

      # Store the article ID and citation count in the hash
      article_citations[article_id] = citation_count

      # Print the citation count for testing
      puts "Citation count for #{article_id}: #{citation_count}"
    rescue Exception => e
      # Handle any errors that may occur during fetching
      article_citations[article_id] = 0

      # Print the error message including the exception class and message
      puts "Error fetching citation count for #{article_id}: #{e.class} - #{e.message}"
    end
  end

  # Return the article citations hash
  article_citations
end

# # Call the function with the array of article IDs
# article_citations = fetch_citation_counts(ARTICLE_IDS)

# # Optionally, you can print the entire article_citations hash for testing
# puts "Article Citations:"
# puts article_citations