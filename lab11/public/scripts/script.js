document.addEventListener("DOMContentLoaded", () => {
  var clientPanel = document.getElementById("clientPanel");

  if (clientPanel) {
    clientPanel.addEventListener("click", () => {
      window.location.href = "/client";
    });
  }

  var adminPanel = document.getElementById("adminPanel");

  if (adminPanel) {
    adminPanel.addEventListener("click", () => {
      window.location.href = "/admin";
    });
  }
});
