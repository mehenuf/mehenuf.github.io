/* ============================================================
   Portfolio — behaviour
   Motion notes live next to each block. Everything obeys
   prefers-reduced-motion via CSS; JS only toggles classes.
   ============================================================ */

/* ---------- THEME (runs immediately, before paint) ----------
   Inlined in <head> as well to avoid a flash of the wrong theme.
   This block is the fallback for pages loading the file only. */
(function () {
  var root = document.documentElement;
  root.classList.add('js');
  if (!root.hasAttribute('data-theme')) {
    var saved = null;
    try { saved = localStorage.getItem('theme'); } catch (e) { /* private mode */ }
    var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    root.setAttribute('data-theme', saved || (prefersDark ? 'dark' : 'light'));
  }
})();

document.addEventListener('DOMContentLoaded', function () {
  var root = document.documentElement;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Theme toggle ----------
     No transition on the swap: colour properties interpolate at
     different rates, so an animated theme change reads as a
     staggered repaint instead of one clean switch. */
  var themeBtn = document.querySelector('.theme-toggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.classList.add('theme-switching');
      root.setAttribute('data-theme', next);
      themeBtn.setAttribute('aria-label', next === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
      try { localStorage.setItem('theme', next); } catch (e) { /* private mode */ }
      // Force a reflow, then re-enable transitions on the next frame.
      void root.offsetHeight;
      requestAnimationFrame(function () {
        requestAnimationFrame(function () { root.classList.remove('theme-switching'); });
      });
    });
  }

  /* ---------- Projects view toggle (grid / list) ---------- */
  var viewBtns = document.querySelectorAll('.view-btn');
  if (viewBtns.length) {
    var currentView = root.getAttribute('data-proj-view') || 'grid';
    viewBtns.forEach(function (btn) {
      btn.setAttribute('aria-pressed', btn.getAttribute('data-view') === currentView ? 'true' : 'false');
      btn.addEventListener('click', function () {
        var view = btn.getAttribute('data-view');
        root.setAttribute('data-proj-view', view);
        viewBtns.forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
        try { localStorage.setItem('projectsView', view); } catch (e) { /* private mode */ }
      });
    });
  }

  /* ---------- Nav: scrolled border + mobile menu ---------- */
  var nav = document.querySelector('.nav');
  var navToggle = document.querySelector('.nav-toggle');
  var navLinks = document.querySelector('.nav-links');

  if (nav) {
    var setScrolled = function () { nav.classList.toggle('scrolled', window.scrollY > 8); };
    setScrolled();
    window.addEventListener('scroll', setScrolled, { passive: true });
  }

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      var open = navLinks.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', String(open));
    });
    navLinks.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navLinks.classList.contains('open')) {
        navLinks.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        navToggle.focus();
      }
    });
  }

  /* ---------- Stagger groups ----------
     Assign delays before the observer runs so children reveal in
     sequence. 60ms apart, capped so a long grid never feels slow. */
  document.querySelectorAll('[data-stagger]').forEach(function (group) {
    Array.prototype.forEach.call(group.children, function (child, i) {
      child.classList.add('reveal');
      child.dataset.delay = String(Math.min(i * 60, 300));
    });
  });

  /* ---------- Calibration readout (the authored focal moment) ----------
     Genuinely numeric .fact values count up from zero like a measurement
     settling on a reading, instead of appearing as static text — the
     literal metaphor behind the "Calibration" design system (see
     DESIGN.md). Only fires on values that actually read as a measurement
     (a leading digit, or one preceded by $/≈/>/</~); qualitative facts
     ("Open to work", "Real-time") are left alone. Runs once, timed to the
     same moment the surrounding .fact tile fades in, and is skipped
     entirely under reduced motion — the real value is already correct
     in the DOM, so skipping loses nothing. */
  var CAL_PREFIX_OK = ['$', '≈', '>', '<', '~'];
  var calFmt = function (c, value) {
    var v = Math.abs(value).toFixed(c.decimals);
    return c.prefix + (c.negative ? c.glyph : '') + v + c.suffix;
  };
  var startCalibration = function (c) {
    if (reduceMotion || c.started) return;
    c.started = true;
    var start = null, dur = 900;
    var step = function (ts) {
      if (!start) start = ts;
      var p = Math.min(1, (ts - start) / dur);
      var eased = 1 - Math.pow(1 - p, 3);
      c.node.data = calFmt(c, c.target * eased);
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  document.querySelectorAll('.fact .k').forEach(function (el) {
    var node = null;
    for (var i = 0; i < el.childNodes.length; i++) {
      if (el.childNodes[i].nodeType === 3 && el.childNodes[i].data && el.childNodes[i].data.trim()) { node = el.childNodes[i]; break; }
    }
    if (!node) return;
    var text = node.data;
    var m = /[-−]?\d[\d.]*/.exec(text);
    if (!m) return;
    var prevChar = m.index > 0 ? text.charAt(m.index - 1) : '';
    if (m.index !== 0 && CAL_PREFIX_OK.indexOf(prevChar) === -1) return;
    var raw = m[0];
    var negative = raw.charAt(0) === '-' || raw.charAt(0) === '−';
    var glyph = raw.charAt(0) === '−' ? '−' : '-';
    var numPart = negative ? raw.slice(1) : raw;
    var num = parseFloat(numPart);
    if (!isFinite(num) || num === 0) return;
    el.__cal = {
      node: node,
      prefix: text.slice(0, m.index),
      suffix: text.slice(m.index + raw.length),
      target: negative ? -num : num,
      decimals: numPart.indexOf('.') > -1 ? numPart.split('.')[1].length : 0,
      negative: negative,
      glyph: glyph,
      started: false
    };
  });

  /* ---------- Scroll reveal (fires once) ---------- */
  var revealEls = document.querySelectorAll('.reveal, .reveal-img');
  if ('IntersectionObserver' in window && revealEls.length) {
    var activate = function (el) {
      el.classList.add('in');
      var kEl = el.classList.contains('fact') ? el.querySelector('.k') : null;
      if (kEl && kEl.__cal) startCalibration(kEl.__cal);
    };
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var delay = Number(entry.target.dataset.delay || 0);
        if (delay) {
          setTimeout(function () { activate(entry.target); }, delay);
        } else {
          activate(entry.target);
        }
        io.unobserve(entry.target);
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });
    revealEls.forEach(function (el) { io.observe(el); });

    /* Safety net. A reveal hides real content, so if anything is still
       hidden while sitting inside the viewport — a late-loading image
       resizing the page, a restored scroll position, a stalled observer —
       show it rather than leaving the reader with a blank band.
       Deliberately NOT tied to the window 'load' event: that waits for
       every image on the page, so one large or slow-loading asset would
       delay the whole safety net right along with it. These timers run
       from script execution instead, independent of asset weight. */
    var sweep = function () {
      document.querySelectorAll('.reveal:not(.in), .reveal-img:not(.in)').forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight && r.bottom > 0) activate(el);
      });
    };
    setTimeout(sweep, 600);
    setTimeout(sweep, 2500);
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- Scroll progress ----------
     A 2px indicator of how far through the page the reader is — useful
     on the longer case-study pages. transform:scaleX only, rAF-throttled
     with the same pattern as the timeline below. Not shown to a reduced-
     motion reader as a moving bar (see CSS): it still reports position,
     just without motion styling drawing the eye. */
  var progressBar = document.querySelector('.scroll-progress .bar');
  if (progressBar) {
    var pTicking = false;
    var updateProgress = function () {
      var doc = document.documentElement;
      var max = doc.scrollHeight - doc.clientHeight;
      var pct = max > 0 ? Math.min(1, Math.max(0, doc.scrollTop / max)) : 0;
      progressBar.style.transform = 'scaleX(' + pct + ')';
      pTicking = false;
    };
    updateProgress();
    window.addEventListener('scroll', function () {
      if (pTicking) return;
      pTicking = true;
      requestAnimationFrame(updateProgress);
    }, { passive: true });
    window.addEventListener('resize', updateProgress);
  }

  /* ---------- Timeline progress ----------
     scaleY on a transform, not height — height would force layout
     on every scroll frame. rAF-throttled so we do at most one
     write per frame no matter how fast the scroll events fire.
     The page now has two independent timelines (Education, Research
     Experience), so every one is tracked, not just the first. */
  var timelines = document.querySelectorAll('.timeline');
  if (timelines.length) {
    var tTicking = false;

    var updateTimelines = function () {
      timelines.forEach(function (timeline) {
        var progress = timeline.querySelector('.t-progress');
        var cursor = timeline.querySelector('.t-cursor');
        var items = timeline.querySelectorAll('.t-item');
        var rect = timeline.getBoundingClientRect();
        var vh = window.innerHeight;
        var total = rect.height || 1;
        var filled = Math.max(0, Math.min(total, vh * 0.7 - rect.top));
        if (progress) progress.style.transform = 'scaleY(' + (filled / total) + ')';
        if (cursor) cursor.style.transform = 'translateY(' + filled + 'px)';

        items.forEach(function (item) {
          if (item.getBoundingClientRect().top < vh * 0.8) item.classList.add('in');
        });
      });
      tTicking = false;
    };

    var onTimelineScroll = function () {
      if (tTicking) return;
      tTicking = true;
      requestAnimationFrame(updateTimelines);
    };

    updateTimelines();
    window.addEventListener('scroll', onTimelineScroll, { passive: true });
    window.addEventListener('resize', onTimelineScroll);
  }

  /* ---------- Skill counts ----------
     Computed from the actual chip count rather than hand-typed, so the
     badge can never drift out of sync if a chip is added or removed. */
  document.querySelectorAll('.skill-card').forEach(function (card) {
    var badge = card.querySelector('.skill-count');
    var count = card.querySelectorAll('.chip-row .chip').length;
    if (badge && count) badge.textContent = count;
  });

  /* ---------- Magnetic tilt (project cards) ----------
     A small, cursor-tracked 3D tilt — the "modern portfolio" card feel,
     kept subtle (6° max) so it reads as fluid rather than gimmicky.
     No CSS transition while the pointer is moving (direct 1:1 tracking
     is what makes it feel physically connected to the cursor); a
     transition is added only for the return-to-neutral on mouseleave.
     rAF-throttled, hover-gated, and skipped entirely under reduced motion —
     a cursor-driven rotation is exactly the kind of motion that spec
     exists to opt out of. */
  var tiltEls = document.querySelectorAll('.proj-card');
  if (tiltEls.length && !reduceMotion && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    var TILT_MAX = 6;
    var cssVar = function (name) { return getComputedStyle(document.documentElement).getPropertyValue(name).trim(); };
    var RESET_EASE = 'transform 500ms ' + cssVar('--ease-out') + ', box-shadow ' + cssVar('--dur-ui') + ' ' + cssVar('--ease-out');

    tiltEls.forEach(function (card) {
      var raf = null, pressed = false, lastX = 0.5, lastY = 0.5;

      var paint = function () {
        var rotY = (lastX - 0.5) * (TILT_MAX * 2);
        var rotX = (0.5 - lastY) * (TILT_MAX * 2);
        var scale = pressed ? 1.0 : 1.012;
        card.style.transition = 'none';
        card.style.transform =
          'perspective(900px) rotateX(' + rotX.toFixed(2) + 'deg) rotateY(' + rotY.toFixed(2) + 'deg) ' +
          'translateY(-4px) scale(' + scale + ')';
        raf = null;
      };

      card.addEventListener('mousemove', function (e) {
        var r = card.getBoundingClientRect();
        lastX = (e.clientX - r.left) / r.width;
        lastY = (e.clientY - r.top) / r.height;
        if (!raf) raf = requestAnimationFrame(paint);
      });
      card.addEventListener('mousedown', function () { pressed = true; if (!raf) raf = requestAnimationFrame(paint); });
      card.addEventListener('mouseup', function () { pressed = false; if (!raf) raf = requestAnimationFrame(paint); });
      card.addEventListener('mouseleave', function () {
        pressed = false;
        if (raf) { cancelAnimationFrame(raf); raf = null; }
        card.style.transition = RESET_EASE;
        card.style.transform = 'none';
      });
    });
  }

  /* ---------- Spotlight glow (skills + leadership cards) ----------
     A soft radial highlight that tracks the pointer — restrained to two
     card types rather than applied everywhere, low opacity, single hue.
     Paints a CSS custom property consumed by a pseudo-element background,
     rAF-throttled so a fast mousemove never issues more than one style
     write per frame. Skipped entirely without a hover-capable pointer. */
  var spotlightEls = document.querySelectorAll('.skill-card, .lead-card');
  if (spotlightEls.length && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    var spotEl = null, spotX = 0, spotY = 0, spotTicking = false;
    var paintSpot = function () {
      if (spotEl) {
        spotEl.style.setProperty('--sx', spotX + 'px');
        spotEl.style.setProperty('--sy', spotY + 'px');
      }
      spotTicking = false;
    };
    spotlightEls.forEach(function (el) {
      el.addEventListener('mousemove', function (e) {
        var r = el.getBoundingClientRect();
        spotEl = el;
        spotX = e.clientX - r.left;
        spotY = e.clientY - r.top;
        if (!spotTicking) { spotTicking = true; requestAnimationFrame(paintSpot); }
      });
    });
  }

  /* ---------- Lightbox ----------
     Occasional frequency, purpose: preventing a jarring change.
     Centered origin — a modal isn't anchored to its trigger. */
  var shots = document.querySelectorAll('.shot');
  if (shots.length) {
    var lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', 'Enlarged image');
    lb.innerHTML =
      '<div class="lightbox-scrim"></div>' +
      '<button class="lightbox-close" aria-label="Close image"><svg viewBox="0 0 24 24" fill="none"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>' +
      '<figure class="lightbox-fig"><img class="lightbox-img" alt=""><figcaption class="lightbox-cap"></figcaption></figure>';
    document.body.appendChild(lb);

    var lbImg = lb.querySelector('.lightbox-img');
    var lbCap = lb.querySelector('.lightbox-cap');
    var lbClose = lb.querySelector('.lightbox-close');
    var lastTrigger = null;

    var openLb = function (src, alt, cap, trigger) {
      lastTrigger = trigger;
      lbImg.src = src;
      lbImg.alt = alt || '';
      lbCap.textContent = cap || '';
      lb.classList.add('open');
      document.body.classList.add('lb-open');
      lbClose.focus();
    };

    var closeLb = function () {
      lb.classList.remove('open');
      document.body.classList.remove('lb-open');
      if (lastTrigger) lastTrigger.focus();
      // Clear the src after the exit finishes so the next open doesn't flash the old image.
      setTimeout(function () { if (!lb.classList.contains('open')) lbImg.src = ''; }, 300);
    };

    shots.forEach(function (shot) {
      shot.addEventListener('click', function () {
        var img = shot.querySelector('img');
        var capEl = shot.querySelector('figcaption b');
        if (img) openLb(img.currentSrc || img.src, img.alt, capEl ? capEl.textContent : '', shot);
      });
    });

    lbClose.addEventListener('click', closeLb);
    lb.querySelector('.lightbox-scrim').addEventListener('click', closeLb);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && lb.classList.contains('open')) closeLb();
    });
    // Trap focus on the only focusable control inside the dialog.
    lb.addEventListener('keydown', function (e) {
      if (e.key === 'Tab' && lb.classList.contains('open')) {
        e.preventDefault();
        lbClose.focus();
      }
    });
  }

  /* ---------- Active section in nav ---------- */
  var sections = document.querySelectorAll('main section[id]');
  var navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');
  if (sections.length && navAnchors.length && 'IntersectionObserver' in window) {
    var secIo = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        navAnchors.forEach(function (a) {
          a.setAttribute('aria-current', String(a.getAttribute('href') === '#' + entry.target.id));
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(function (s) { secIo.observe(s); });
  }

  /* ---------- Footer year ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
});
