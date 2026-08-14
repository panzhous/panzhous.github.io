(() => {
  const explorer = document.querySelector("[data-publication-explorer]");
  if (!explorer) return;

  const list = explorer.querySelector("[data-publication-list]");
  const controls = explorer.querySelector(".publication-controls");
  const items = [...list.querySelectorAll(".publication-item")];
  const yearGroups = [...list.querySelectorAll(":scope > [data-publication-year-group]")];
  const resultCount = explorer.querySelector("[data-publication-count]");
  const lineButtons = [...explorer.querySelectorAll("[data-research-line-filter]")];
  const subtopics = explorer.querySelector("[data-publication-subtopics]");
  const subtopicGroups = [...explorer.querySelectorAll("[data-subtopic-group]")];
  const dropdowns = [...explorer.querySelectorAll("[data-filter-dropdown]")];

  let selectedLine = "all";
  let selectedSubtopic = "all";

  function setPressed(buttons, activeValue, attribute) {
    buttons.forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset[attribute] === activeValue));
    });
  }

  function closeDropdown(dropdown) {
    dropdown.classList.remove("is-open");
    dropdown.querySelector("[data-filter-trigger]").setAttribute("aria-expanded", "false");
  }

  function openDropdown(dropdown) {
    dropdowns.forEach((item) => {
      if (item !== dropdown) closeDropdown(item);
    });
    dropdown.classList.add("is-open");
    dropdown.querySelector("[data-filter-trigger]").setAttribute("aria-expanded", "true");
  }

  function setDropdownLabel(button) {
    const dropdown = button.closest("[data-filter-dropdown]");
    dropdown.querySelector("[data-filter-label]").textContent = button.textContent.trim();
    closeDropdown(dropdown);
  }

  function updateSubtopics() {
    subtopicGroups.forEach((group) => {
      const isActive = group.dataset.subtopicGroup === selectedLine;
      group.hidden = !isActive;
      if (!isActive) {
        group.querySelector("[data-filter-label]").textContent = "All";
        closeDropdown(group);
        group.querySelectorAll("[data-subtopic-filter]").forEach((button) => button.setAttribute("aria-pressed", "false"));
      }
    });

    const activeGroup = subtopicGroups.find((group) => group.dataset.subtopicGroup === selectedLine);
    subtopics.hidden = !activeGroup;
    if (activeGroup) {
      setPressed([...activeGroup.querySelectorAll("[data-subtopic-filter]")], selectedSubtopic, "subtopicFilter");
    }
  }

  dropdowns.forEach((dropdown) => {
    const trigger = dropdown.querySelector("[data-filter-trigger]");

    dropdown.addEventListener("pointerenter", (event) => {
      if (event.pointerType === "mouse") openDropdown(dropdown);
    });
    dropdown.addEventListener("pointerleave", (event) => {
      if (event.pointerType === "mouse") closeDropdown(dropdown);
    });
    dropdown.addEventListener("focusin", () => openDropdown(dropdown));
    dropdown.addEventListener("focusout", (event) => {
      if (!dropdown.contains(event.relatedTarget)) closeDropdown(dropdown);
    });
    trigger.addEventListener("click", (event) => {
      event.stopPropagation();
      openDropdown(dropdown);
    });
  });

  document.addEventListener("click", (event) => {
    dropdowns.forEach((dropdown) => {
      if (!dropdown.contains(event.target)) closeDropdown(dropdown);
    });
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") dropdowns.forEach(closeDropdown);
  });

  function applyFilters() {
    let visibleCount = 0;
    const visibleYears = new Set();

    items.forEach((item) => {
      const matchesLine = selectedLine === "all" || item.dataset.researchLine === selectedLine;
      const matchesSubtopic = selectedSubtopic === "all" || item.dataset.subtopic === selectedSubtopic;
      const isVisible = matchesLine && matchesSubtopic;

      item.hidden = !isVisible;
      if (isVisible) {
        visibleCount += 1;
        visibleYears.add(item.dataset.year);
      }
    });

    yearGroups.forEach((group) => {
      group.hidden = !visibleYears.has(group.dataset.year);
    });

    resultCount.textContent = `${visibleCount} publication${visibleCount === 1 ? "" : "s"}`;
  }

  lineButtons.forEach((button) => {
    button.addEventListener("click", () => {
      selectedLine = button.dataset.researchLineFilter;
      selectedSubtopic = "all";
      setPressed(lineButtons, selectedLine, "researchLineFilter");
      setDropdownLabel(button);
      updateSubtopics();
      applyFilters();
    });
  });

  subtopicGroups.forEach((group) => {
    group.querySelectorAll("[data-subtopic-filter]").forEach((button) => {
      button.addEventListener("click", () => {
        selectedSubtopic = button.dataset.subtopicFilter;
        setDropdownLabel(button);
        updateSubtopics();
        applyFilters();
      });
    });
  });

  updateSubtopics();
  applyFilters();
  controls.hidden = false;
})();
