/* Turns the email links from _includes/email-link.html into working mailto: links.
   The address is only put together here, so it never appears in the page's code. */
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('a.dyn-email[data-u][data-d]').forEach(function (link) {
    link.href = 'mailto:' + link.getAttribute('data-u') + '@' + link.getAttribute('data-d');
  });
});
