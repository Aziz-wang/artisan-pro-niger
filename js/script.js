document.addEventListener("DOMContentLoaded", function () {

  // ======================
  // NAVBAR MOBILE
  // ======================
  const toggle = document.getElementById("menu-toggle");
  const nav = document.getElementById("nav-links");

  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      nav.classList.toggle("active");
    });

    document.querySelectorAll(".nav-links a").forEach(link => {
      link.addEventListener("click", () => {
        nav.classList.remove("active");
      });
    });
  }

  // ======================
  // SCROLL ANIMATION
  // ======================
  const elements = document.querySelectorAll(".fade-in");

  function show() {
    elements.forEach(el => {
      if (el.getBoundingClientRect().top < window.innerHeight - 100) {
        el.classList.add("visible");
      }
    });
  }

  show();
  window.addEventListener("scroll", show);

});
