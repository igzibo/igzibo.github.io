// Set active navigation link
function setActiveNav() {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-links a');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href && href.startsWith("/") && (href === "/" ? currentPath === "/" : currentPath === href || currentPath.startsWith(href))) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
}

// Add the shared Policies menu to pages created before policy navigation existed.
function addPoliciesNav() {
  const navLinks = document.querySelector('.nav-links');
  if (!navLinks || navLinks.querySelector('.nav-dropdown')) {
    return;
  }

  const policyCategories = [
    ['Client Services', '/policies/client-services/'],
    ['Corporate', '/policies/corporate/'],
    ['Governance', '/policies/governance/'],
    ['Privacy', '/policies/privacy/'],
    ['Recruiting', '/policies/recruiting/'],
    ['Security', '/policies/security/'],
    ['Website', '/policies/website/']
  ];
  const policyItem = document.createElement('li');
  policyItem.className = 'nav-dropdown';
  policyItem.innerHTML = '<a href="/policies/">Policies</a><ul class="nav-dropdown-menu">' +
    policyCategories.map(([name, href]) => `<li><a href="${href}">${name}</a></li>`).join('') +
    '</ul>';
  navLinks.insertBefore(policyItem, navLinks.querySelector('.btn')?.parentElement || null);
}

// Run on page load
document.addEventListener('DOMContentLoaded', () => {
  addPoliciesNav();
  setActiveNav();
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});
