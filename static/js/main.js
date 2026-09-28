/* Suresh Shahi — site interactions */

/* Mobile menu */
const menu = document.querySelector('.menu');
const nav = document.querySelector('.site-header nav');
if (menu && nav) menu.addEventListener('click', () => nav.classList.toggle('open'));
document.querySelectorAll('.site-header nav a').forEach(a => a.addEventListener('click', () => nav?.classList.remove('open')));

/* Scroll-triggered reveal (single system used everywhere, incl. staggered groups) */
const revealObserver = new IntersectionObserver(entries => entries.forEach(entry => {
  if (entry.isIntersecting) {
    entry.target.classList.add('visible');
    revealObserver.unobserve(entry.target);
  }
}), { threshold: .08 });
document.querySelectorAll('.reveal, .reveal-stagger').forEach(el => revealObserver.observe(el));

/* Inject the scroll-progress bar and back-to-top button once, before wiring listeners */
if (!document.querySelector('.scroll-progress')) {
  const bar = document.createElement('div');
  bar.className = 'scroll-progress';
  document.body.prepend(bar);
}
if (!document.querySelector('.to-top')) {
  const btn = document.createElement('button');
  btn.className = 'to-top';
  btn.setAttribute('aria-label', 'Back to top');
  btn.innerHTML = '<i class="fa-solid fa-arrow-up"></i>';
  btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  document.body.appendChild(btn);
}

/* Header: solid on scroll + scroll progress bar */
const header = document.querySelector('.site-header');
const progress = document.querySelector('.scroll-progress');
let ticking = false;
function onScroll() {
  const y = window.scrollY || document.documentElement.scrollTop;
  if (header) header.classList.toggle('scrolled', y > 8);
  if (progress) {
    const h = document.documentElement;
    const max = h.scrollHeight - h.clientHeight;
    progress.style.width = (max > 0 ? Math.min(100, (y / max) * 100) : 0) + '%';
  }
  const toTop = document.querySelector('.to-top');
  if (toTop) toTop.classList.toggle('show', y > 500);
  ticking = false;
}
window.addEventListener('scroll', () => { if (!ticking) { requestAnimationFrame(onScroll); ticking = true; } }, { passive: true });
onScroll();

/* Active nav link = section currently in view (home page only) */
const sections = [...document.querySelectorAll('main [id]')];
const navLinks = [...document.querySelectorAll('.site-header nav a[href*="#"]')];
if (sections.length && navLinks.length) {
  const sectionObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const id = entry.target.id;
      navLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href')?.endsWith('#' + id)));
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  sections.forEach(s => sectionObserver.observe(s));
}
