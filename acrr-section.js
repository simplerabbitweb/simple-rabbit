/* ── ACRR CHECKLIST SECTION ─────────────────────────────────────────────────
   Edit the HTML below to update this section on every blog post at once.
   Injected above the "More Articles" 3-card section on all posts.
   ────────────────────────────────────────────────────────────────────────── */

(function () {
  var html = `
<!-- ACRR CHECKLIST PROMO -->
<div style="padding:48px 0;">
  <div style="max-width:960px; margin:0 auto; padding:0 24px;">
    <div style="background:#849aa9; display:flex; align-items:stretch; overflow:hidden; border-radius:4px; flex-wrap:wrap;">
      <img src="/acrr-checklist.png" alt="ACRR Checklist" style="width:320px; flex-shrink:0; display:block; object-fit:cover; align-self:stretch;">
      <div style="flex:1; min-width:260px; padding:48px 48px;">
        <p style="font-size:11px; font-weight:600; letter-spacing:2px; text-transform:uppercase; color:rgba(255,255,255,0.65); margin-bottom:16px;">Free Resource</p>
        <h2 style="font-family:'Instrument Serif', Georgia, serif; font-size:clamp(28px,4vw,42px); font-weight:400; color:#fff; line-height:1.15; margin-bottom:20px;">Score Your Practice</h2>
        <p style="font-size:16px; line-height:1.65; color:rgba(255,255,255,0.8); margin-bottom:32px;">Placeholder copy — paste your section content here and deploy.</p>
        <a href="https://simplerabbit.myflodesk.com/acrr-checklist" target="_blank" rel="noopener"
           style="display:inline-block; background:#0A0905; color:#FDFAF7; padding:14px 40px; font-size:13px; font-weight:600; letter-spacing:1.5px; text-transform:uppercase; font-family:'DM Sans',system-ui,sans-serif; text-decoration:none; transition:background 0.2s;">
          Get the Checklist &rarr;
        </a>
      </div>
    </div>
  </div>
</div>
`;

  var el = document.getElementById('acrr-section');
  if (el) el.outerHTML = html;
})();
