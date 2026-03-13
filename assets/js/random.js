/**
 * Random person redirect.
 * Loads search.json, picks a random person, redirects to their page.
 */
(function () {
  'use strict';

  var B = (document.querySelector('base') || {}).href || '/';

  fetch(B + 'search.json')
    .then(function (r) { return r.json(); })
    .then(function (data) {
      var person = data[Math.floor(Math.random() * data.length)];
      window.location.replace(B + 'en/people/' + person.id + '.html');
    })
    .catch(function () {
      document.getElementById('random-status').textContent = 'Failed to load. Try again.';
    });
})();
