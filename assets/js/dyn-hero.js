/* Banner video: the small icon button in the banner's corner pauses and restarts it. The choice is remembered
   in this browser, so a visitor who paused it gets the banners paused on the next pages too */
document.addEventListener('DOMContentLoaded', function () {
  var hero = document.querySelector('.dyn-hero');
  var video = hero && hero.querySelector('.dyn-hero__video');
  var button = hero && hero.querySelector('.dyn-hero__pause');
  if (!video || !button) {
    return;
  }

  var storageKey = 'dyn-hero-paused';
  var paused = false;
  try {
    paused = window.localStorage.getItem(storageKey) === '1';
  } catch (e) {
    // storage blocked (private window, cookies off): the button still works, it just isn't remembered
  }

  function apply() {
    if (paused) {
      video.pause();
    } else {
      var playing = video.play();
      if (playing && playing.catch) {
        playing.catch(function () {});
      }
    }
    var label = paused ? 'Play the background video' : 'Pause the background video';
    button.setAttribute('aria-label', label);
    button.setAttribute('title', label);
    hero.classList.toggle('is-paused', paused);
  }

  if (paused) {
    video.removeAttribute('autoplay');
  }
  apply();
  button.hidden = false;

  button.addEventListener('click', function () {
    paused = !paused;
    try {
      if (paused) {
        window.localStorage.setItem(storageKey, '1');
      } else {
        window.localStorage.removeItem(storageKey);
      }
    } catch (e) {
      // not remembered, see above
    }
    apply();
  });
});
