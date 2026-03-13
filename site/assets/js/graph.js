/**
 * Relation graph visualization for person pages.
 * Uses Cytoscape.js to render an interactive network graph.
 */
(function () {
  'use strict';

  var B = (document.querySelector('base') || {}).href || '/';

  var container = document.getElementById('relation-graph');
  if (!container) return;

  var personId = container.dataset.person;
  if (!personId) return;

  var COLORS = {
    same_field: '#4a90d9',
    same_country: '#d9534f',
    same_era: '#5cb85c'
  };

  var LABELS = {
    same_field: 'Same Field',
    same_country: 'Same Country',
    same_era: 'Same Era'
  };

  fetch(B + 'generated/links/people/' + personId + '.json')
    .then(function (res) {
      if (!res.ok) throw new Error('No relation data');
      return res.json();
    })
    .then(function (data) { render(data); })
    .catch(function () {
      container.style.display = 'none';
    });

  function render(data) {
    var nodes = [];
    var edges = [];
    var seen = {};

    // Center node
    nodes.push({
      data: {
        id: personId,
        label: nameFromId(personId),
        isCenter: true
      }
    });
    seen[personId] = true;

    // Limit each relation type to 8 nodes to keep the graph readable
    var MAX_PER_TYPE = 8;

    ['same_field', 'same_country', 'same_era'].forEach(function (key) {
      var ids = (data[key] || []).slice(0, MAX_PER_TYPE);
      ids.forEach(function (rid) {
        if (!seen[rid]) {
          nodes.push({
            data: {
              id: rid,
              label: nameFromId(rid),
              isCenter: false
            }
          });
          seen[rid] = true;
        }
        edges.push({
          data: {
            source: personId,
            target: rid,
            relationType: key
          }
        });
      });
    });

    if (nodes.length < 2) {
      container.style.display = 'none';
      return;
    }

    var cy = cytoscape({
      container: container,
      elements: { nodes: nodes, edges: edges },
      style: [
        {
          selector: 'node',
          style: {
            'label': 'data(label)',
            'text-valign': 'bottom',
            'text-halign': 'center',
            'font-size': '11px',
            'font-family': 'system-ui, sans-serif',
            'text-margin-y': 6,
            'background-color': '#888',
            'width': 28,
            'height': 28,
            'border-width': 2,
            'border-color': '#666',
            'text-wrap': 'wrap',
            'text-max-width': '90px',
            'cursor': 'pointer'
          }
        },
        {
          selector: 'node[?isCenter]',
          style: {
            'background-color': '#ff9800',
            'border-color': '#e65100',
            'border-width': 3,
            'width': 44,
            'height': 44,
            'font-size': '13px',
            'font-weight': 'bold',
            'text-margin-y': 8
          }
        },
        {
          selector: 'edge',
          style: {
            'width': 2,
            'curve-style': 'bezier',
            'opacity': 0.6
          }
        },
        {
          selector: 'edge[relationType="same_field"]',
          style: { 'line-color': COLORS.same_field }
        },
        {
          selector: 'edge[relationType="same_country"]',
          style: { 'line-color': COLORS.same_country }
        },
        {
          selector: 'edge[relationType="same_era"]',
          style: { 'line-color': COLORS.same_era }
        }
      ],
      layout: {
        name: 'concentric',
        concentric: function (node) {
          return node.data('isCenter') ? 10 : 1;
        },
        levelWidth: function () { return 1; },
        minNodeSpacing: 50,
        animate: false
      },
      userZoomingEnabled: true,
      userPanningEnabled: true,
      boxSelectionEnabled: false
    });

    // Click to navigate
    cy.on('tap', 'node', function (evt) {
      var id = evt.target.id();
      window.location.href = B + 'en/people/' + id + '.html';
    });

    // Hover cursor
    cy.on('mouseover', 'node', function () {
      container.style.cursor = 'pointer';
    });
    cy.on('mouseout', 'node', function () {
      container.style.cursor = 'default';
    });

    // Build legend
    var legend = document.getElementById('graph-legend');
    if (legend) {
      var html = '';
      ['same_field', 'same_country', 'same_era'].forEach(function (key) {
        if (data[key] && data[key].length > 0) {
          html += '<span style="display:inline-flex;align-items:center;margin-right:16px;">'
            + '<span style="display:inline-block;width:20px;height:3px;background:'
            + COLORS[key] + ';margin-right:6px;"></span>'
            + LABELS[key] + '</span>';
        }
      });
      legend.innerHTML = html;
    }
  }

  function nameFromId(id) {
    // Convert slug to display name: "albert-einstein" → "Albert Einstein"
    return id.split('-').map(function (w) {
      if (w.length === 0) return w;
      return w.charAt(0).toUpperCase() + w.slice(1);
    }).join(' ');
  }
})();
