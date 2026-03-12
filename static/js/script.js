function toggleMenu() {

  const menu = document.getElementById("fullscreen-menu");
  const icon = document.querySelector(".menu-icon");

  menu.classList.toggle("active");
  icon.classList.toggle("open");

}

document.querySelectorAll("#fullscreen-menu a").forEach(link => {
  link.addEventListener("click", () => {
    document.getElementById("fullscreen-menu").classList.remove("active");
    document.querySelector(".menu-icon").classList.remove("open");
  });
});

