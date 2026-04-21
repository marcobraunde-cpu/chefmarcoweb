const toggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
if (toggle) {
  toggle.addEventListener('click', () => navLinks.classList.toggle('open'));
}

const current = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-links a').forEach(a => {
  if (a.getAttribute('href') === current) a.classList.add('active');
});
