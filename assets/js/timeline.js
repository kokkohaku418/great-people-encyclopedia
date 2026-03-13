/**
 * Interactive horizontal timeline of historical figures.
 * Uses D3.js to render birth points on a scrollable timeline from -500 to 2025.
 */
(function () {
  'use strict';

  var FIELD_COLORS = {
    physics: '#4a90d9',
    mathematics: '#9b59b6',
    chemistry: '#e67e22',
    biology: '#27ae60',
    philosophy: '#8e44ad',
    politics: '#c0392b',
    engineering: '#2c3e50',
    astronomy: '#2980b9',
    literature: '#d4a017',
    art: '#e74c3c'
  };

  var MIN_YEAR = -500;
  var MAX_YEAR = 2025;
  var ROW_HEIGHT = 20;
  var MARGIN = { top: 60, right: 40, bottom: 40, left: 40 };
  var DOT_RADIUS = 5;

  var container = document.getElementById('timeline-container');
  if (!container) return;

  // Tooltip
  var tooltip = document.createElement('div');
  tooltip.id = 'tl-tooltip';
  document.body.appendChild(tooltip);

  fetch('/search.json')
    .then(function (r) { return r.json(); })
    .then(function (data) { render(data); })
    .catch(function () {
      container.innerHTML = '<p>Failed to load data.</p>';
    });

  function render(raw) {
    // Filter to people with valid birth_year in range
    var people = raw.filter(function (p) {
      return p.birth_year != null && p.birth_year >= MIN_YEAR && p.birth_year <= MAX_YEAR;
    }).sort(function (a, b) {
      return a.birth_year - b.birth_year;
    });

    var width = Math.max(container.clientWidth, 960);
    // Place dots in lanes to avoid overlap
    var lanes = assignLanes(people, width);
    var height = MARGIN.top + (lanes.maxLane + 1) * ROW_HEIGHT + MARGIN.bottom;

    var svg = d3.select(container)
      .append('svg')
      .attr('width', width)
      .attr('height', height);

    // Scale
    var x = d3.scaleLinear()
      .domain([MIN_YEAR, MAX_YEAR])
      .range([MARGIN.left, width - MARGIN.right]);

    // Axis
    var tickValues = [];
    for (var y = Math.ceil(MIN_YEAR / 100) * 100; y <= MAX_YEAR; y += 100) {
      tickValues.push(y);
    }
    var axis = d3.axisTop(x)
      .tickValues(tickValues)
      .tickFormat(function (d) {
        if (d < 0) return Math.abs(d) + ' BCE';
        return '' + d;
      });

    svg.append('g')
      .attr('transform', 'translate(0,' + MARGIN.top + ')')
      .call(axis)
      .selectAll('text')
      .attr('font-size', '11px');

    // Era bands
    var eras = [
      { label: 'Classical', start: -500, end: 500, color: 'rgba(155,89,182,0.06)' },
      { label: 'Medieval', start: 500, end: 1300, color: 'rgba(52,152,219,0.06)' },
      { label: 'Renaissance', start: 1300, end: 1600, color: 'rgba(230,126,34,0.06)' },
      { label: 'Enlightenment', start: 1600, end: 1800, color: 'rgba(39,174,96,0.06)' },
      { label: 'Industrial', start: 1800, end: 1900, color: 'rgba(192,57,43,0.06)' },
      { label: 'Modern', start: 1900, end: 1970, color: 'rgba(44,62,80,0.06)' },
      { label: 'Contemporary', start: 1970, end: 2025, color: 'rgba(41,128,185,0.06)' }
    ];

    eras.forEach(function (era) {
      var ex = x(Math.max(era.start, MIN_YEAR));
      var ew = x(Math.min(era.end, MAX_YEAR)) - ex;
      svg.append('rect')
        .attr('x', ex).attr('y', MARGIN.top)
        .attr('width', ew).attr('height', height - MARGIN.top - MARGIN.bottom)
        .attr('fill', era.color);
      svg.append('text')
        .attr('x', ex + ew / 2).attr('y', MARGIN.top + 14)
        .attr('text-anchor', 'middle')
        .attr('font-size', '10px')
        .attr('fill', '#999')
        .text(era.label);
    });

    // Dots
    svg.selectAll('.person-dot')
      .data(lanes.items)
      .enter()
      .append('circle')
      .attr('class', 'person-dot')
      .attr('cx', function (d) { return x(d.birth_year); })
      .attr('cy', function (d) { return MARGIN.top + 24 + d._lane * ROW_HEIGHT; })
      .attr('r', DOT_RADIUS)
      .attr('fill', function (d) { return FIELD_COLORS[(d.fields || [])[0]] || '#888'; })
      .attr('stroke', '#fff')
      .attr('stroke-width', 1)
      .style('cursor', 'pointer')
      .on('mouseover', function (event, d) {
        d3.select(this).attr('r', DOT_RADIUS + 3).attr('stroke-width', 2);
        var field = (d.fields || [])[0] || '';
        var years = d.birth_year + (d.death_year ? ' – ' + d.death_year : ' – present');
        tooltip.innerHTML = '<strong>' + esc(d.name) + '</strong><br>' + years + '<br><em>' + field + '</em>';
        tooltip.style.display = 'block';
      })
      .on('mousemove', function (event) {
        tooltip.style.left = (event.pageX + 12) + 'px';
        tooltip.style.top = (event.pageY - 10) + 'px';
      })
      .on('mouseout', function () {
        d3.select(this).attr('r', DOT_RADIUS).attr('stroke-width', 1);
        tooltip.style.display = 'none';
      })
      .on('click', function (event, d) {
        window.location.href = '/en/people/' + d.id + '.html';
      });

    // Lifespan lines (optional subtle line from birth to death)
    svg.selectAll('.lifespan-line')
      .data(lanes.items.filter(function (d) { return d.death_year; }))
      .enter()
      .append('line')
      .attr('class', 'lifespan-line')
      .attr('x1', function (d) { return x(d.birth_year); })
      .attr('x2', function (d) { return x(Math.min(d.death_year, MAX_YEAR)); })
      .attr('y1', function (d) { return MARGIN.top + 24 + d._lane * ROW_HEIGHT; })
      .attr('y2', function (d) { return MARGIN.top + 24 + d._lane * ROW_HEIGHT; })
      .attr('stroke', function (d) { return FIELD_COLORS[(d.fields || [])[0]] || '#888'; })
      .attr('stroke-width', 1.5)
      .attr('opacity', 0.2)
      .lower();

    // Legend
    var legendDiv = document.getElementById('timeline-legend');
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
  }

  function assignLanes(people, width) {
    // Greedy lane assignment: each lane tracks the rightmost occupied x pixel
    var x = d3.scaleLinear().domain([MIN_YEAR, MAX_YEAR]).range([MARGIN.left, width - MARGIN.right]);
    var laneEnds = []; // rightmost pixel used per lane
    var minGap = DOT_RADIUS * 2 + 2;
    var maxLane = 0;

    people.forEach(function (p) {
      var px = x(p.birth_year);
      var placed = false;
      for (var i = 0; i < laneEnds.length; i++) {
        if (px - laneEnds[i] >= minGap) {
          p._lane = i;
          var endX = p.death_year ? x(Math.min(p.death_year, MAX_YEAR)) : px;
          laneEnds[i] = Math.max(endX, px) + minGap;
          placed = true;
          break;
        }
      }
      if (!placed) {
        p._lane = laneEnds.length;
        var endX = p.death_year ? x(Math.min(p.death_year, MAX_YEAR)) : px;
        laneEnds.push(Math.max(endX, px) + minGap);
      }
      if (p._lane > maxLane) maxLane = p._lane;
    });

    return { items: people, maxLane: maxLane };
  }

  function esc(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
})();
