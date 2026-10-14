/* Sidebar: the menu button opens the menu on small screens,
   and each item's arrow button opens its sub-menu underneath */
document.addEventListener('DOMContentLoaded', function () {
  var sidebar = document.querySelector('.dyn-sidebar');
  if (!sidebar) {
    return;
  }

  var menuButton = sidebar.querySelector('.dyn-sidebar__menu-btn');
  if (menuButton) {
    menuButton.addEventListener('click', function () {
      var open = sidebar.classList.toggle('is-open');
      menuButton.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  sidebar.querySelectorAll('.dyn-sidebar__toggle').forEach(function (button) {
    button.addEventListener('click', function () {
      var item = button.closest('.dyn-sidebar__item-wrap');
      var open = item.classList.toggle('is-open');
      button.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
});
