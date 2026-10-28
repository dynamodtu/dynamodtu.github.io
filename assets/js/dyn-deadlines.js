/* Open positions close on their own: the site is only rebuilt when something is pushed, so this checks each
   deadline (data-deadline="YYYY-MM-DD", the last day to apply) against today's date in Denmark.
   After the deadline:
   - data-when="open" elements are hidden (the deadline sentence, the position on the Contact page),
     data-when="closed" ones are shown (the "Closed" label, "This position is closed");
   - data-closed-class="..." elements get that class (the greyed-out text of the post);
   - a data-deadline-group (the Contact page's list of positions) is hidden when none is open any more. */
document.addEventListener('DOMContentLoaded', function () {
  var today;
  try {
    // "sv-SE" writes dates as YYYY-MM-DD
    today = new Intl.DateTimeFormat('sv-SE', { timeZone: 'Europe/Copenhagen' }).format(new Date());
  } catch (e) {
    today = new Date().toISOString().slice(0, 10);
  }

  document.querySelectorAll('[data-deadline]').forEach(function (el) {
    var closed = today > el.getAttribute('data-deadline');
    var when = el.getAttribute('data-when');
    if (when === 'open') {
      el.hidden = closed;
    } else if (when === 'closed') {
      el.hidden = !closed;
    }
    var closedClass = el.getAttribute('data-closed-class');
    if (closedClass) {
      el.classList.toggle(closedClass, closed);
    }
  });

  document.querySelectorAll('[data-deadline-group]').forEach(function (group) {
    group.hidden = !group.querySelector('[data-when="open"]:not([hidden])');
  });
});
