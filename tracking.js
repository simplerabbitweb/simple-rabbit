(function () {
  // Safe gtag wrapper — page_title included on every event
  function track(eventName, params) {
    if (typeof gtag === 'function') {
      gtag('event', eventName, Object.assign({
        page_location: window.location.href,
        page_title: document.title
      }, params || {}));
    }
  }

  // 1) book_consult_click — any element with [data-book]
  document.querySelectorAll('[data-book]').forEach(function (el) {
    el.addEventListener('click', function () {
      track('book_consult_click', {
        button_text: (el.innerText || '').trim().slice(0, 100)
      });
    });
  });

  // 2) phone_click — tel: links
  document.querySelectorAll('a[href^="tel:"]').forEach(function (el) {
    el.addEventListener('click', function () {
      track('phone_click', {
        phone_number: el.getAttribute('href').replace('tel:', '')
      });
    });
  });

  // 3) insurance_check — FAQ row with [data-faq="insurance"]
  var ins = document.querySelector('[data-faq="insurance"]');
  if (ins) {
    var insFired = false;
    var insHandler = function () {
      if (insFired) return;
      insFired = true;
      track('insurance_check', { question: 'insurance' });
    };
    ins.addEventListener('click', insHandler);
    ins.addEventListener('toggle', function () { if (ins.open) insHandler(); });
  }

  // 4) engaged_session — fires once after 60s of active time on page
  //    Pauses when tab is hidden or window loses focus
  var activeMs = 0, lastTick = Date.now(), engagedFired = false;
  function isActive() {
    return document.visibilityState === 'visible' && document.hasFocus();
  }
  setInterval(function () {
    var now = Date.now();
    if (isActive()) activeMs += (now - lastTick);
    lastTick = now;
    if (!engagedFired && activeMs >= 60000) {
      engagedFired = true;
      track('engaged_session', { engagement_seconds: 60 });
    }
  }, 1000);

})();
