/**
 * World map visualization of historical figures using Leaflet.js.
 * Loads search.json, groups people by country, places markers on a map.
 */
(function () {
  'use strict';

  // Country code → [lat, lng, name]
  var COORDS = {
    af: [33.93, 67.71, 'Afghanistan'], ao: [-8.84, 13.23, 'Angola'],
    ar: [-34.60, -58.38, 'Argentina'], at: [48.21, 16.37, 'Austria'],
    au: [-33.87, 151.21, 'Australia'], bd: [23.81, 90.41, 'Bangladesh'],
    be: [50.85, 4.35, 'Belgium'], bg: [42.70, 23.32, 'Bulgaria'],
    br: [-15.79, -47.88, 'Brazil'], by: [53.90, 27.57, 'Belarus'],
    ca: [45.42, -75.70, 'Canada'], cd: [-4.32, 15.31, 'DR Congo'],
    ch: [46.95, 7.45, 'Switzerland'], cl: [-33.45, -70.67, 'Chile'],
    cn: [39.90, 116.40, 'China'], co: [4.71, -74.07, 'Colombia'],
    cu: [23.11, -82.37, 'Cuba'], cz: [50.08, 14.44, 'Czech Republic'],
    de: [52.52, 13.41, 'Germany'], dk: [55.68, 12.57, 'Denmark'],
    dz: [36.75, 3.04, 'Algeria'], eg: [30.04, 31.24, 'Egypt'],
    es: [40.42, -3.70, 'Spain'], et: [9.02, 38.75, 'Ethiopia'],
    fi: [60.17, 24.94, 'Finland'], fr: [48.86, 2.35, 'France'],
    gb: [51.51, -0.13, 'United Kingdom'], gh: [5.56, -0.19, 'Ghana'],
    gn: [9.64, -13.58, 'Guinea'], gr: [37.98, 23.73, 'Greece'],
    ht: [18.54, -72.34, 'Haiti'], hu: [47.50, 19.04, 'Hungary'],
    id: [-6.21, 106.85, 'Indonesia'], ie: [53.35, -6.26, 'Ireland'],
    il: [31.77, 35.23, 'Israel'], in: [28.61, 77.21, 'India'],
    iq: [33.31, 44.37, 'Iraq'], ir: [35.69, 51.39, 'Iran'],
    is: [64.15, -21.94, 'Iceland'], it: [41.90, 12.50, 'Italy'],
    jm: [18.00, -76.79, 'Jamaica'], jp: [35.68, 139.69, 'Japan'],
    ke: [-1.29, 36.82, 'Kenya'], kh: [11.56, 104.92, 'Cambodia'],
    kp: [39.02, 125.75, 'North Korea'], kr: [37.57, 126.98, 'South Korea'],
    kz: [51.17, 71.43, 'Kazakhstan'], lc: [14.01, -60.99, 'Saint Lucia'],
    lk: [6.93, 79.84, 'Sri Lanka'], ls: [-29.31, 27.48, 'Lesotho'],
    lt: [54.69, 25.28, 'Lithuania'], lv: [56.95, 24.11, 'Latvia'],
    ma: [33.97, -6.85, 'Morocco'], ml: [12.64, -8.00, 'Mali'],
    mm: [19.76, 96.07, 'Myanmar'], mn: [47.92, 106.91, 'Mongolia'],
    mq: [14.62, -61.06, 'Martinique'], mx: [19.43, -99.13, 'Mexico'],
    my: [3.14, 101.69, 'Malaysia'], ng: [9.06, 7.49, 'Nigeria'],
    ni: [12.11, -86.24, 'Nicaragua'], nl: [52.37, 4.90, 'Netherlands'],
    no: [59.91, 10.75, 'Norway'], nz: [-41.29, 174.78, 'New Zealand'],
    pe: [-12.05, -77.04, 'Peru'], ph: [14.60, 120.98, 'Philippines'],
    pk: [33.69, 73.04, 'Pakistan'], pl: [52.23, 21.01, 'Poland'],
    pt: [38.72, -9.14, 'Portugal'], rs: [44.79, 20.47, 'Serbia'],
    ru: [55.76, 37.62, 'Russia'], se: [59.33, 18.07, 'Sweden'],
    sg: [1.35, 103.82, 'Singapore'], sn: [14.72, -17.47, 'Senegal'],
    sy: [33.51, 36.29, 'Syria'], th: [13.76, 100.50, 'Thailand'],
    tn: [36.81, 10.18, 'Tunisia'], tr: [39.93, 32.85, 'Turkey'],
    tz: [-6.79, 39.28, 'Tanzania'], ua: [50.45, 30.52, 'Ukraine'],
    us: [38.91, -77.04, 'United States'], uz: [41.30, 69.28, 'Uzbekistan'],
    ve: [10.49, -66.88, 'Venezuela'], vn: [21.03, 105.85, 'Vietnam'],
    za: [-33.93, 18.42, 'South Africa']
  };

  var FIELD_COLORS = {
    physics: '#4a90d9', mathematics: '#9b59b6', chemistry: '#e67e22',
    biology: '#27ae60', philosophy: '#8e44ad', politics: '#c0392b',
    engineering: '#2c3e50', astronomy: '#2980b9', literature: '#d4a017',
    art: '#e74c3c'
  };

  var mapEl = document.getElementById('world-map');
  if (!mapEl) return;

  var map = L.map('world-map', {
    center: [20, 0],
    zoom: 2,
    minZoom: 2,
    maxZoom: 8,
    worldCopyJump: true
  });

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    maxZoom: 18
  }).addTo(map);

  fetch('/search.json')
    .then(function (r) { return r.json(); })
    .then(function (data) { plotPeople(data); })
    .catch(function () {
      mapEl.innerHTML = '<p style="padding:20px;">Failed to load data.</p>';
    });

  function plotPeople(people) {
    // Group by country
    var byCountry = {};
    people.forEach(function (p) {
      (p.countries || []).forEach(function (c) {
        if (!byCountry[c]) byCountry[c] = [];
        byCountry[c].push(p);
      });
    });

    var markers = L.markerClusterGroup({
      maxClusterRadius: 40,
      spiderfyOnMaxZoom: true,
      showCoverageOnHover: false,
      iconCreateFunction: function (cluster) {
        var count = cluster.getChildCount();
        var size = count > 50 ? 'large' : count > 20 ? 'medium' : 'small';
        return L.divIcon({
          html: '<div>' + count + '</div>',
          className: 'cluster-icon cluster-' + size,
          iconSize: L.point(40, 40)
        });
      }
    });

    Object.keys(byCountry).forEach(function (code) {
      var coord = COORDS[code];
      if (!coord) return;
      var countryPeople = byCountry[code].sort(function (a, b) {
        return a.name.localeCompare(b.name);
      });

      // Spread markers slightly within the same country to avoid exact overlap
      countryPeople.forEach(function (p, i) {
        var angle = (i / countryPeople.length) * 2 * Math.PI;
        var spread = Math.min(countryPeople.length * 0.04, 2.0);
        var lat = coord[0] + Math.sin(angle) * spread * (0.3 + Math.random() * 0.7);
        var lng = coord[1] + Math.cos(angle) * spread * (0.3 + Math.random() * 0.7);

        var field = (p.fields || [])[0] || '';
        var color = FIELD_COLORS[field] || '#888';

        var icon = L.divIcon({
          html: '<div style="background:' + color + ';width:12px;height:12px;border-radius:50%;border:2px solid #fff;box-shadow:0 1px 3px rgba(0,0,0,0.3);"></div>',
          className: 'person-marker',
          iconSize: [16, 16],
          iconAnchor: [8, 8]
        });

        var years = p.birth_year + (p.death_year ? '–' + p.death_year : '–present');
        var popupHtml = '<div style="font-family:system-ui,sans-serif;min-width:140px;">'
          + '<strong><a href="/en/people/' + p.id + '.html" style="color:#1a0dab;">' + esc(p.name) + '</a></strong><br>'
          + '<span style="font-size:12px;color:#666;">' + years + '</span><br>'
          + '<span style="font-size:12px;color:' + color + ';">' + field + '</span>'
          + '</div>';

        var marker = L.marker([lat, lng], { icon: icon }).bindPopup(popupHtml);
        markers.addLayer(marker);
      });
    });

    map.addLayer(markers);

    // Build legend
    var legendDiv = document.getElementById('map-legend');
    if (legendDiv) {
      var html = '';
      Object.keys(FIELD_COLORS).sort().forEach(function (f) {
        html += '<span style="display:inline-flex;align-items:center;margin-right:14px;margin-bottom:4px;">'
          + '<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:'
          + FIELD_COLORS[f] + ';margin-right:5px;"></span>'
          + f.charAt(0).toUpperCase() + f.slice(1) + '</span>';
      });
      legendDiv.innerHTML = html;
    }

    // Stats
    var statsDiv = document.getElementById('map-stats');
    if (statsDiv) {
      statsDiv.textContent = people.length + ' people across ' + Object.keys(byCountry).length + ' countries';
    }
  }

  function esc(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
})();
