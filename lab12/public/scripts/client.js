// public/clients.js

document.addEventListener("DOMContentLoaded", function () {
  // Get references to the product elements
  const mercedesImage = document.getElementById("mercedes");
  const bmwImage = document.getElementById("bmw");
  const fiatImage = document.getElementById("fiat");
  const volvoImage = document.getElementById("volvo");

  // Add click event listeners
  mercedesImage.addEventListener("click", function () {
    sellProduct("Mercedes");
  });

  bmwImage.addEventListener("click", function () {
    sellProduct("BMW");
  });

  fiatImage.addEventListener("click", function () {
    sellProduct("Fiat");
  });

  volvoImage.addEventListener("click", function () {
    sellProduct("Volvo");
  });

  // Function to handle selling a product
  async function sellProduct(productName) {
    try {
      // Make an asynchronous request to the server
      const response = await fetch(`/sellProduct/${productName}`, {
        method: "POST",
      });

      // Check if the request was successful (status code 200)
      if (response.ok) {
        const productData = await response.json();
        alert(`Sold ${productData.name} for ${productData.value}`);
      } else {
        console.error("Error selling product:", response.statusText);
      }
    } catch (error) {
      console.error("Error selling product:", error);
    }
  }
});
