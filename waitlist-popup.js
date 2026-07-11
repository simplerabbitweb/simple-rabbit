/* Simple Rabbit — AI Front Desk waitlist popup.
   Shows once per visit (session) on first scroll. Reappears on a new visit. */
(function () {
  if (window.__srWaitlistInit) return;
  window.__srWaitlistInit = true;

  // Normalize path and skip funnel / utility / the AI page itself (form already there)
  var path = location.pathname.replace(/\/index\.html$/, '/').replace(/\.html$/, '');
  if (path.length > 1) path = path.replace(/\/$/, '');
  var EXCLUDE = ['/ai-front-desk', '/apply', '/thank-you', '/contact', '/changes',
                 '/client-hub', '/privacy-policy', '/404', '/media-kit'];
  if (EXCLUDE.indexOf(path) !== -1) return;

  // Once per visit. sessionStorage resets on a new visit (new tab/session).
  try { if (sessionStorage.getItem('srWaitlistShown')) return; } catch (e) {}

  var shown = false;

  function injectCss() {
    var s = document.createElement('style');
    s.textContent =
      '#sr-wl{position:fixed;inset:0;z-index:99999;display:flex;align-items:center;justify-content:center;padding:20px;background:rgba(10,9,5,0.55);opacity:0;transition:opacity .3s ease;}' +
      '#sr-wl.on{opacity:1;}' +
      '#sr-wl-card{position:relative;background:#FDFAF7;max-width:460px;width:100%;padding:46px 40px 40px;box-shadow:0 24px 80px rgba(0,0,0,0.28);transform:translateY(14px);transition:transform .3s ease;max-height:92vh;overflow:auto;}' +
      '#sr-wl.on #sr-wl-card{transform:translateY(0);}' +
      '#sr-wl-close{position:absolute;top:12px;right:16px;background:none;border:none;font-size:28px;line-height:1;color:#7A756E;cursor:pointer;padding:4px;}' +
      '#sr-wl-close:hover{color:#0A0905;}' +
      '#sr-wl .eb{font-family:"DM Sans",system-ui,sans-serif;font-size:11px;font-weight:600;letter-spacing:2.5px;text-transform:uppercase;color:#AA737D;display:block;margin-bottom:12px;}' +
      '#sr-wl h3{font-family:"Instrument Serif",Georgia,serif;font-size:32px;line-height:1.05;letter-spacing:-1px;font-weight:400;color:#0A0905;margin:0 0 12px;}' +
      '#sr-wl p.sub{font-family:"DM Sans",system-ui,sans-serif;font-size:15px;line-height:1.6;color:#4A4540;margin:0 0 24px;}' +
      '#sr-wl label{display:block;font-family:"DM Sans",system-ui,sans-serif;font-size:12px;font-weight:600;letter-spacing:0.4px;color:#0A0905;margin-bottom:6px;}' +
      '#sr-wl input{width:100%;padding:12px 14px;font-family:"DM Sans",system-ui,sans-serif;font-size:15px;color:#0A0905;background:#fff;border:1px solid rgba(0,0,0,0.14);margin-bottom:16px;border-radius:2px;}' +
      '#sr-wl input:focus{outline:none;border-color:#AA737D;}' +
      '#sr-wl button.sub-btn{width:100%;background:#474D73;color:#fff;border:none;padding:15px;font-family:"DM Sans",system-ui,sans-serif;font-size:14px;font-weight:600;letter-spacing:1px;text-transform:uppercase;cursor:pointer;transition:background .2s;}' +
      '#sr-wl button.sub-btn:hover{background:#2D3154;}' +
      '#sr-wl button.sub-btn:disabled{background:#7A756E;cursor:not-allowed;}' +
      '#sr-wl .ok{text-align:center;}';
    document.head.appendChild(s);
  }

  function build() {
    injectCss();
    var o = document.createElement('div');
    o.id = 'sr-wl';
    o.setAttribute('role', 'dialog');
    o.setAttribute('aria-modal', 'true');
    o.innerHTML =
      '<div id="sr-wl-card">' +
        '<button id="sr-wl-close" aria-label="Close">&times;</button>' +
        '<div id="sr-wl-body">' +
          '<span class="eb">Coming Fall 2026</span>' +
          '<h3>Never send another patient to voicemail.</h3>' +
          '<p class="sub">An AI front desk that answers your phone and website, books appointments, and follows up. Join the waitlist for early access.</p>' +
          '<form id="sr-wl-form" action="https://formspree.io/f/xnjeaaeo" method="POST">' +
            '<label for="sr-wl-name">Your name</label>' +
            '<input id="sr-wl-name" type="text" name="name" autocomplete="name">' +
            '<label for="sr-wl-email">Email *</label>' +
            '<input id="sr-wl-email" type="email" name="email" required autocomplete="email">' +
            '<label for="sr-wl-practice">Practice name</label>' +
            '<input id="sr-wl-practice" type="text" name="practice">' +
            '<input type="hidden" name="source" value="site popup">' +
            '<button type="submit" class="sub-btn">Join the Waitlist &rarr;</button>' +
          '</form>' +
        '</div>' +
      '</div>';
    document.body.appendChild(o);
    requestAnimationFrame(function () { o.classList.add('on'); });

    function close() {
      o.classList.remove('on');
      setTimeout(function () { if (o.parentNode) o.parentNode.removeChild(o); }, 300);
      document.removeEventListener('keydown', esc);
    }
    function esc(e) { if (e.key === 'Escape') close(); }
    document.getElementById('sr-wl-close').addEventListener('click', close);
    o.addEventListener('click', function (e) { if (e.target === o) close(); });
    document.addEventListener('keydown', esc);

    var form = document.getElementById('sr-wl-form');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var b = form.querySelector('button.sub-btn');
      b.disabled = true; b.textContent = 'Joining...';
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'Accept': 'application/json' } })
        .then(function (r) {
          if (r.ok) {
            document.getElementById('sr-wl-body').innerHTML =
              '<div class="ok"><span class="eb">Coming Fall 2026</span>' +
              '<h3>You’re on the list.</h3>' +
              '<p class="sub">I’ll reach out with early access before Fall 2026. Talk soon.</p></div>';
          } else { b.disabled = false; b.innerHTML = 'Join the Waitlist &rarr;'; }
        })
        .catch(function () { b.disabled = false; b.innerHTML = 'Join the Waitlist &rarr;'; });
    });
  }

  function show() {
    if (shown) return;
    shown = true;
    try { sessionStorage.setItem('srWaitlistShown', '1'); } catch (e) {}
    window.removeEventListener('scroll', onScroll);
    build();
  }
  function onScroll() { if (window.scrollY > 60) show(); }
  window.addEventListener('scroll', onScroll, { passive: true });
})();
