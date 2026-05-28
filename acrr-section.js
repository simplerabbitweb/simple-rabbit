/* ── ACRR CHECKLIST SECTION ─────────────────────────────────────────────────
   Edit the HTML below to update this section on every blog post at once.
   Injected before the footer on all posts.
   ────────────────────────────────────────────────────────────────────────── */

(function () {
  var html = `
<!-- ACRR CHECKLIST PROMO -->
<style>
  @media(max-width:768px){
    .acrr-grid{grid-template-columns:1fr !important; min-height:auto !important;}
    .acrr-img{height:280px !important;}
    .acrr-text{padding:48px 32px !important;}
  }
</style>
<section style="background:var(--bg); padding:0; border-bottom:1px solid var(--rule-vt); overflow:hidden;">
  <div class="acrr-grid" style="display:grid; grid-template-columns:1fr 1fr; min-height:500px;">
    <div class="acrr-img" style="overflow:hidden; position:relative; min-height:360px;">
      <img src="/acrr-checklist.png" alt="ACRR Patient Acquisition Checklist" style="position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;">
    </div>
    <div class="acrr-text" style="padding:80px 64px; display:flex; flex-direction:column; justify-content:center;">
      <h2 style="font-family:var(--font-d); font-size:clamp(28px,3vw,48px); line-height:1.1; letter-spacing:-1.5px; font-weight:300; color:var(--white); margin-bottom:24px;">
        Is your private-pay practice ready for <em>consistent patient growth?</em>
      </h2>
      <p style="font-size:17px; line-height:1.8; color:var(--mid-vt); margin-bottom:40px;">Most private-pay practitioners are excellent at the medicine and unsure about the marketing. The ACRR Patient Acquisition Checklist shows you exactly where your patient acquisition stands.</p>
      <div>
        <a href="https://simplerabbit.myflodesk.com/acrr-checklist" target="_blank" rel="noopener"
           style="display:inline-block; background:var(--white); color:var(--black); padding:16px 48px; font-size:15px; font-weight:600; letter-spacing:1.2px; text-transform:uppercase; font-family:var(--font-b); text-decoration:none;">
          Score Your Practice &rarr;
        </a>
      </div>
    </div>
  </div>
</section>
`;

  var el = document.getElementById('acrr-section');
  if (el) el.outerHTML = html;
})();
