/**
 * Dynamic filtering for the People index page.
 * Loads search.json, builds filter dropdowns, renders a filterable list.
 */
(function () {
  'use strict';

  var B = (document.querySelector('base') || {}).href || '/';

  var container = document.getElementById('people-filter-app');
  if (!container) return;

  // Era definitions (must match data/eras/)
  var ERAS = [
    { id: 'ancient',       label: 'Ancient',       start: -3000, end: -500 },
    { id: 'classical',     label: 'Classical',      start: -500,  end: 500 },
    { id: 'medieval',      label: 'Medieval',       start: 500,   end: 1300 },
    { id: 'renaissance',   label: 'Renaissance',    start: 1300,  end: 1600 },
    { id: 'enlightenment', label: 'Enlightenment',  start: 1600,  end: 1800 },
    { id: 'industrial',    label: 'Industrial',     start: 1800,  end: 1900 },
    { id: 'modern',        label: 'Modern',         start: 1900,  end: 1970 },
    { id: 'contemporary',  label: 'Contemporary',   start: 1970,  end: 2030 }
  ];

  // Read field/country labels embedded by the generator
  var fieldLabels = {};
  var countryLabels = {};
  try {
    fieldLabels = JSON.parse(document.getElementById('field-labels').textContent);
    countryLabels = JSON.parse(document.getElementById('country-labels').textContent);
  } catch (e) { /* fallback to raw IDs */ }

  var people = [];
  var fieldSelect, countrySelect, eraSelect, countEl, listEl;

  // Build UI
  function buildUI() {
    var style = document.createElement('style');
    style.textContent = [
      '#people-filter-app { font-family: system-ui, sans-serif; }',
      '.filter-bar { display: flex; flex-wrap: wrap; gap: 12px; align-items: end; margin-bottom: 20px; padding: 16px; background: #f5f5f5; border-radius: 8px; }',
      '.filter-group { display: flex; flex-direction: column; gap: 4px; }',
      '.filter-group label { font-size: 13px; font-weight: 600; color: #555; }',
      '.filter-group select { padding: 6px 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 14px; min-width: 160px; background: #fff; }',
      '.filter-count { font-size: 14px; color: #666; margin-bottom: 12px; }',
      '#people-list { list-style: none; padding: 0; column-count: 3; column-gap: 24px; }',
      '#people-list li { break-inside: avoid; padding: 3px 0; }',
      '#people-list a { color: #1a0dab; text-decoration: none; font-size: 14px; }',
      '#people-list a:hover { text-decoration: underline; }',
      '@media (max-width: 768px) { #people-list { column-count: 2; } }',
      '@media (max-width: 480px) { #people-list { column-count: 1; } .filter-bar { flex-direction: column; } }'
    ].join('\n');
    document.head.appendChild(style);

    var html = '<div class="filter-bar">';
    html += '<div class="filter-group"><label for="filter-field">Field</label><select id="filter-field"><option value="">All Fields</option></select></div>';
    html += '<div class="filter-group"><label for="filter-country">Country</label><select id="filter-country"><option value="">All Countries</option></select></div>';
    html += '<div class="filter-group"><label for="filter-era">Era</label><select id="filter-era"><option value="">All Eras</option></select></div>';
    html += '</div>';
    html += '<div id="people-count" class="filter-count"></div>';
    html += '<ul id="people-list"></ul>';

    container.innerHTML = html;

    fieldSelect = document.getElementById('filter-field');
    countrySelect = document.getElementById('filter-country');
    eraSelect = document.getElementById('filter-era');
    countEl = document.getElementById('people-count');
    listEl = document.getElementById('people-list');

    fieldSelect.addEventListener('change', applyFilters);
    countrySelect.addEventListener('change', applyFilters);
    eraSelect.addEventListener('change', applyFilters);
  }

  function getEra(birthYear) {
    if (birthYear == null) return null;
    for (var i = 0; i < ERAS.length; i++) {
      if (birthYear >= ERAS[i].start && birthYear < ERAS[i].end) {
        return ERAS[i].id;
      }
    }
    return null;
  }

  function populateDropdowns() {
    var fieldSet = {};
    var countrySet = {};

    people.forEach(function (p) {
      (p.fields || []).forEach(function (f) { fieldSet[f] = true; });
      (p.countries || []).forEach(function (c) { countrySet[c] = true; });
    });

    // Fields sorted by label
    Object.keys(fieldSet).sort(function (a, b) {
      var la = fieldLabels[a] || a, lb = fieldLabels[b] || b;
      return la.localeCompare(lb);
    }).forEach(function (f) {
      var opt = document.createElement('option');
      opt.value = f;
      opt.textContent = fieldLabels[f] || f;
      fieldSelect.appendChild(opt);
    });

    // Countries sorted by label
    Object.keys(countrySet).sort(function (a, b) {
      var la = countryLabels[a] || a, lb = countryLabels[b] || b;
      return la.localeCompare(lb);
    }).forEach(function (c) {
      var opt = document.createElement('option');
      opt.value = c;
      opt.textContent = countryLabels[c] || c;
      countrySelect.appendChild(opt);
    });

    // Eras in chronological order
    ERAS.forEach(function (era) {
      var opt = document.createElement('option');
      opt.value = era.id;
      opt.textContent = era.label;
      eraSelect.appendChild(opt);
    });
  }

  function applyFilters() {
    var field = fieldSelect.value;
    var country = countrySelect.value;
    var era = eraSelect.value;

    var filtered = people.filter(function (p) {
      if (field && (p.fields || []).indexOf(field) === -1) return false;
      if (country && (p.countries || []).indexOf(country) === -1) return false;
      if (era && getEra(p.birth_year) !== era) return false;
      return true;
    });

    countEl.textContent = 'Showing ' + filtered.length + ' of ' + people.length + ' people';

    var html = '';
    filtered.forEach(function (p) {
      html += '<li><a href="' + B + 'en/people/' + p.id + '.html">' + escHtml(p.name) + '</a></li>';
    });
    listEl.innerHTML = html;
  }

  function escHtml(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  // Init
  buildUI();
  fetch(B + 'search.json')
    .then(function (res) { return res.json(); })
    .then(function (data) {
      people = data.sort(function (a, b) { return a.name.localeCompare(b.name); });
      populateDropdowns();
      applyFilters();
    })
    .catch(function (err) {
      container.innerHTML = '<p>Failed to load people data.</p>';
    });
})();
