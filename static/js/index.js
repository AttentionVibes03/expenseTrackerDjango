document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("sidebar");
    const windowWidth = window.innerWidth;
  
    // Check window width on page load and adjust sidebar
    if (windowWidth < 768) {
      sidebar.classList.add("d-none");
    }
  
    // Toggle sidebar on button click
    const toggleButton = document.getElementById("toggle-sidebar");
    if (toggleButton) {
      toggleButton.addEventListener("click", function () {
        sidebar.classList.toggle("d-none");
      });
    }
  
    // Update sidebar visibility when the window is resized
    window.addEventListener("resize", function () {
      const newWindowWidth = window.innerWidth;
      if (newWindowWidth < 768) {
        sidebar.classList.add("d-none");
      } else {
        sidebar.classList.remove("d-none");
      }
    });
  });
  