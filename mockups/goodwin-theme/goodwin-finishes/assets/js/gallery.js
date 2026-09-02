/**
 * Goodwin Decorative Finishes — filters, enquiry form, nav.
 * No dependencies, no build step.
 */
(function () {
	'use strict';

	var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

	/* ── Reveal on scroll ── */
	var revealables = document.querySelectorAll('.reveal, .tile');

	if (reduced || !('IntersectionObserver' in window)) {
		revealables.forEach(function (el) { el.classList.add('in'); });
	} else {
		var io = new IntersectionObserver(function (entries) {
			entries.forEach(function (e) {
				if (e.isIntersecting) {
					e.target.classList.add('in');
					io.unobserve(e.target);
				}
			});
		}, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });

		revealables.forEach(function (el, i) {
			el.style.transitionDelay = (i % 5) * 60 + 'ms';
			io.observe(el);
		});
	}

	/* ── Filters ── */
	var filters = document.getElementById('filters');
	var countEl = document.getElementById('count');

	if (filters) {
		var tiles = Array.prototype.slice.call(document.querySelectorAll('.tile'));

		var apply = function (slug) {
			var shown = 0;

			tiles.forEach(function (tile) {
				var cats = (tile.getAttribute('data-cats') || '').split(' ');
				var show = slug === 'all' || cats.indexOf(slug) !== -1;

				tile.classList.toggle('is-hidden', !show);
				if (show) {
					shown++;
					tile.classList.add('in');
				}
			});

			if (countEl) {
				var word = shown === 1 ? countEl.getAttribute('data-singular') : countEl.getAttribute('data-plural');
				countEl.textContent = shown + ' ' + word;
			}

			Array.prototype.forEach.call(filters.querySelectorAll('button'), function (b) {
				b.setAttribute('aria-pressed', String(b.getAttribute('data-filter') === slug));
			});

			// Keep the choice in the URL so a filtered view can be linked to.
			if (window.history && window.history.replaceState) {
				var url = slug === 'all'
					? window.location.pathname
					: window.location.pathname + '?finish=' + encodeURIComponent(slug);
				window.history.replaceState(null, '', url);
			}
		};

		filters.addEventListener('click', function (e) {
			var btn = e.target.closest('button');
			if (btn) { apply(btn.getAttribute('data-filter')); }
		});

		// Finish cards elsewhere on the page jump here and apply their filter.
		document.querySelectorAll('[data-jump]').forEach(function (link) {
			link.addEventListener('click', function () {
				apply(link.getAttribute('data-jump'));
			});
		});

		// Honour ?finish=slug on load.
		var initial = new URLSearchParams(window.location.search).get('finish');
		if (initial && filters.querySelector('[data-filter="' + CSS.escape(initial) + '"]')) {
			apply(initial);
		}
	}

	/* ── Enquiry form: posts straight to the endpoint, stays on the page ── */
	var form = document.getElementById('quoteform');

	if (form) {
		var statusEl = document.getElementById('formstatus');

		form.addEventListener('submit', function (e) {
			e.preventDefault();

			var btn = form.querySelector('button[type="submit"]');
			statusEl.textContent = 'Sending…';
			btn.disabled = true;

			fetch(form.action, {
				method: 'POST',
				body: new FormData(form),
				headers: { Accept: 'application/json' }
			})
				.then(function (r) {
					if (r.ok) { return; }
					return r.json().then(function (d) {
						throw new Error((d.errors || []).map(function (x) { return x.message; }).join(', ') || 'That did not send.');
					});
				})
				.then(function () {
					form.innerHTML =
						'<p class="label">Thank you</p>' +
						'<p class="lede" style="color:rgba(237,234,225,.8);margin:0">Your enquiry is on its way. Lauren will be in touch within two business days.</p>';
				})
				.catch(function (err) {
					statusEl.textContent = err.message + ' Email ' + form.dataset.email + ' instead.';
					btn.disabled = false;
				});
		});
	}

	/* ── Header ── */
	var topbar = document.getElementById('topbar');
	if (topbar) {
		var stick = function () {
			topbar.classList.toggle('is-stuck', window.scrollY > 40);
		};
		stick();
		window.addEventListener('scroll', stick, { passive: true });
	}

	var nav = document.getElementById('nav');
	var navtoggle = document.getElementById('navtoggle');

	if (nav && navtoggle) {
		navtoggle.addEventListener('click', function () {
			var open = nav.classList.toggle('is-open');
			navtoggle.setAttribute('aria-expanded', String(open));
			navtoggle.textContent = open ? 'Close' : 'Menu';
		});

		nav.addEventListener('click', function (e) {
			if (e.target.tagName === 'A') {
				nav.classList.remove('is-open');
				navtoggle.textContent = 'Menu';
				navtoggle.setAttribute('aria-expanded', 'false');
			}
		});
	}
}());
