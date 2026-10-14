/* Year filter on the Publications page: "All" shows every year, a year button shows only that year */
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.dyn-years').forEach(function (bar) {
    var category = bar.closest('.dyn-pubs__category');
    bar.hidden = false;
    bar.addEventListener('click', function (event) {
      var button = event.target.closest('button[data-year]');
      if (!button) {
        return;
      }
      var year = button.getAttribute('data-year');
      bar.querySelectorAll('button').forEach(function (b) {
        b.setAttribute('aria-pressed', b === button ? 'true' : 'false');
      });
      category.querySelectorAll('.dyn-pubs__year-group').forEach(function (group) {
        group.hidden = year !== 'all' && group.getAttribute('data-year') !== year;
      });
    });
  });
});
