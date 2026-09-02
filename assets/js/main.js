/**
* Template Name: Laura
* Updated: Mar 10 2023 with Bootstrap v5.2.3
* Template URL: https://bootstrapmade.com/laura-free-creative-bootstrap-theme/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    if (!header.classList.contains('header-scrolled')) {
      offset -= 20
    }

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Skills animation
   */
  let skilsContent = select('.skills-content');
  if (skilsContent) {
    new Waypoint({
      element: skilsContent,
      offset: '80%',
      handler: function(direction) {
        let progress = select('.progress .progress-bar', true);
        progress.forEach((el) => {
          el.style.width = el.getAttribute('aria-valuenow') + '%'
        });
      }
    })
  }

  /**
   * Baseball timing mini game
   */
  const game = select('#baseball-game');
  if (game) {
    const ball = select('#baseball');
    const swingButton = select('#swing-button');
    const message = select('#game-message');
    const scoreDisplay = select('#game-score');
    const streakDisplay = select('#game-streak');
    const bestDisplay = select('#game-best');
    let animationFrame;
    let pitchStartedAt;
    let pitchDuration;
    let ballPosition = 6;
    let isPitching = false;
    let score = 0;
    let streak = 0;
    let best = 0;

    try {
      best = Number(window.localStorage.getItem('baseball-best-streak')) || 0;
    } catch (error) {
      best = 0;
    }
    bestDisplay.textContent = best;

    const updateStats = () => {
      scoreDisplay.textContent = score;
      streakDisplay.textContent = streak;
      bestDisplay.textContent = best;
    };

    const setMessage = (text, type = '') => {
      message.textContent = text;
      message.classList.remove('success', 'miss');
      if (type) message.classList.add(type);
    };

    const saveBest = () => {
      if (streak <= best) return;
      best = streak;
      try {
        window.localStorage.setItem('baseball-best-streak', String(best));
      } catch (error) {
        // The game still works when browser storage is unavailable.
      }
    };

    const endPitch = (text, type) => {
      isPitching = false;
      window.cancelAnimationFrame(animationFrame);
      ball.classList.remove('is-pitching');
      swingButton.textContent = 'Next pitch';
      setMessage(text, type);
      updateStats();
    };

    const missPitch = () => {
      streak = 0;
      endPitch('Strike — that one got past you.', 'miss');
    };

    const animatePitch = (timestamp) => {
      if (!pitchStartedAt) pitchStartedAt = timestamp;
      const progress = Math.min((timestamp - pitchStartedAt) / pitchDuration, 1);
      ballPosition = 6 + (progress * 88);
      ball.style.left = `${ballPosition}%`;

      if (progress < 1 && isPitching) {
        animationFrame = window.requestAnimationFrame(animatePitch);
      } else if (isPitching) {
        missPitch();
      }
    };

    const startPitch = () => {
      window.cancelAnimationFrame(animationFrame);
      isPitching = true;
      pitchStartedAt = 0;
      pitchDuration = 1700 + (Math.random() * 850);
      ballPosition = 6;
      ball.style.left = '6%';
      ball.classList.add('is-pitching');
      swingButton.textContent = 'Swing!';
      setMessage('Watch the ball…');
      animationFrame = window.requestAnimationFrame(animatePitch);
    };

    const swing = () => {
      if (!isPitching) {
        startPitch();
        return;
      }

      if (ballPosition >= 49 && ballPosition <= 54) {
        score += 4;
        streak += 1;
        saveBest();
        endPitch('Home run! Perfect timing. +4 runs', 'success');
      } else if (ballPosition >= 45 && ballPosition <= 58) {
        score += 1;
        streak += 1;
        saveBest();
        endPitch('Base hit! Nice contact. +1 run', 'success');
      } else {
        streak = 0;
        endPitch(ballPosition < 45 ? 'Too early — strike.' : 'Too late — strike.', 'miss');
      }
    };

    swingButton.addEventListener('click', swing);
    document.addEventListener('keydown', (event) => {
      const tagName = document.activeElement?.tagName;
      if (event.code === 'Space' && isPitching && !['INPUT', 'TEXTAREA', 'SELECT'].includes(tagName)) {
        event.preventDefault();
        swing();
      }
    });
  }

})()
