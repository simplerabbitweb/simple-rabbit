(function () {
  if (typeof gtag === 'undefined') return;

  function fire(event, params) {
    gtag('event', event, Object.assign({ page_location: window.location.href }, params));
  }

  // 1. book_consult_click — every CTA that links to /contact
  document.querySelectorAll('a[href="/contact"]').forEach(function (el) {
    el.addEventListener('click', function () {
      fire('book_consult_click', { button_text: el.innerText.trim() });
    });
  });

  // 3. phone_click — tel: links (footer phone numbers on blog posts)
  document.querySelectorAll('a[href^="tel:"]').forEach(function (el) {
    el.addEventListener('click', function () {
      fire('phone_click', { phone_number: el.getAttribute('href').replace('tel:', '') });
    });
  });

  // 4. engaged_session — fires after 60 continuous seconds on page (pauses when tab is hidden)
  var engagedFired = false;
  var engagedTimer = null;
  function startEngagedTimer() {
    if (engagedFired) return;
    engagedTimer = setTimeout(function () {
      engagedFired = true;
      fire('engaged_session');
    }, 60000);
  }
  function stopEngagedTimer() {
    clearTimeout(engagedTimer);
  }
  startEngagedTimer();
  document.addEventListener('visibilitychange', function () {
    document.hidden ? stopEngagedTimer() : startEngagedTimer();
  });

  // 5. insurance_check — fires once when an insurance-related FAQ row scrolls into view
  var insEls = document.querySelectorAll('[data-track="insurance_check"]');
  if (insEls.length && 'IntersectionObserver' in window) {
    var insObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting && !entry.target._srTracked) {
          entry.target._srTracked = true;
          fire('insurance_check', { question: 'insurance' });
          insObs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    insEls.forEach(function (el) { insObs.observe(el); });
  }

})();
