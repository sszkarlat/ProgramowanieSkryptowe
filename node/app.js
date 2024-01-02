const http = require("http");
const fs = require("fs");
const path = require("path");
const { parse } = require("querystring");

const clientsFile = path.join(__dirname, "clients.json");
const productsFile = path.join(__dirname, "products.json");

let clientsData = readJsonFile(clientsFile) || [];
let productsData = readJsonFile(productsFile) || [];

function readJsonFile(filename) {
  try {
    const data = fs.readFileSync(filename, "utf8");
    return JSON.parse(data);
  } catch (error) {
    console.error(`Error reading file ${filename}:`, error.message);
    return null;
  }
}

function writeJsonFile(filename, jsonData) {
  try {
    const data = JSON.stringify(jsonData, null, 2);
    fs.writeFileSync(filename, data, "utf8");
    console.log(`Data written to ${filename}`);
  } catch (error) {
    console.error(`Error writing to file ${filename}:`, error.message);
  }
}

function requestListener(request, response) {
  console.log("--------------------------------------");
  console.log(`The relative URL of the current request: ${request.url}`);
  console.log(`Access method: ${request.method}`);
  console.log("--------------------------------------");

  const url = new URL(request.url, `http://${request.headers.host}`);

  if (url.pathname === "/favicon.ico") {
    response.writeHead(200, { "Content-Type": "image/x-icon" });
    fs.createReadStream(path.join(__dirname, "favicon.ico")).pipe(response);
    return;
  }

  if (url.pathname.startsWith("/pictures/") && request.method === "GET") {
    const imagePath = path.join(__dirname, url.pathname);
    const imageStream = fs.createReadStream(imagePath);

    imageStream.on("open", function () {
      response.setHeader("Content-Type", "image/jpeg");
      imageStream.pipe(response);
    });

    imageStream.on("error", function () {
      response.writeHead(404);
      response.end("Not Found");
    });

    return;
  }
  /* ******** */
  /* "Routes" */
  /* ******** */

  /* ---------------- */
  /* Route "GET('/')" */
  /* ---------------- */
  if (url.pathname === "/" && request.method === "GET") {
    response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });

    response.write(`<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    
    <style>
        @keyframes rotation {
    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}

#commandLine {
    width: 20%;
}

#shopContainer {
    background-color: #FED777;
    text-align: center;
    padding: 20px;
}

#fotter {
    background-color: green;
}

div>.azure>img {
    border-top-left-radius: 2%;
    border-top-right-radius: 2%;
    width: 100%;
}

.azure:hover {
    animation-name: rotation;
    animation-iteration-count: infinite;
    animation-duration: 10s;
    animation-direction: forwards;
    animation-play-state: running;
}

.azure {
    border-style: solid;
    border-color: #A8A8A8;
    border-width: 2px;
    border-radius: 3%;
    animation-name: rotation;
    animation-iteration-count: infinite;
    animation-duration: 10s;
    animation-direction: forwards;
    animation-play-state: paused;
    margin-left: 75px;
    margin-right: 75px;
}

h4 {
    padding-top: 10px;
    padding-left: 10px;
    padding-right: 10px;
}


h2 {
    padding-bottom: 10px;
}

.navbar-collapse {
    flex-grow: 0;
}

@media screen and (min-width: 600px) {
    #mercedes {
        margin-right: 20px;
        width: 50%;
        height: 70%;
    }

    #fiat {
        width: 30%;
        height: 20%;
    }

    #volvo {
        margin-right: 20px;
        width: 30%;
        height: 30%;
    }

    #bmw {
        width: 30%;
        height: 100%;
    }
}

@media screen and (max-width: 600px) {
    #volvo {
        width: 70%;
        position: relative;
        left: 30%;
    }

    #bmw {
        width: 50%;
    }
}
    </style>

    <script>
      document.addEventListener("DOMContentLoaded", function () {
        // Add event listener only if the form is found
        var form = document.getElementById("myForm");
        if (form) {
          form.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent the default form submission
            executeCommandonServer();
          });
        }
      });

      function executeCommandonServer() {
        var commandLine = document.getElementById("commandLine").value;
      }
        function draw() {
            "use strict";
            var canvas = document.getElementById("canvas");
            var ctx = canvas.getContext("2d");

            //Rysuj samochod
            ctx.beginPath();
            ctx.moveTo(2 + 1.5, 40 - 15);
            ctx.lineTo(8 + 1.5, 32 - 15);
            ctx.lineTo(30.6 + 1.5, 32 - 15);
            ctx.arc(30 + 1.5, 36 - 15, 4, 30, 2 * Math.PI);
            ctx.lineTo(34 + 1.5, 36 - 15);
            ctx.lineTo(34 + 1.5, 40 - 15);
            ctx.lineTo(42 + 1.5, 40 - 15);
            ctx.arc(42 + 1.5, 44 - 15, 4, 30, 2 * Math.PI);
            ctx.lineTo(46 + 1.5, 48 - 15);
            ctx.lineTo(37.4 + 1.5, 48 - 15);
            ctx.lineTo(13.6 + 1.5, 48 - 15);
            ctx.lineTo(2 + 1.5, 48 - 15);
            ctx.lineTo(2 + 1.5, 40 - 15);
            ctx.fillStyle = "#F3D723";
            ctx.fill();
            ctx.stroke();

            //Rysuj okna
            ctx.beginPath();
            ctx.moveTo(8 + 2.5, 36 - 11);
            ctx.lineTo(8 + 2.5, 32 - 12);
            ctx.lineTo(30.6 - 2.5, 32 - 12);
            ctx.arc(30 - 2.5, 36 - 12, 4, 30, 2 * Math.PI);
            ctx.lineTo(34 - 2.5, 36 - 11);
            ctx.lineTo(34 - 2.5, 36 - 11);
            ctx.lineTo(8 + 2.5, 36 - 11);
            ctx.fillStyle = "#898888";
            ctx.fill();
            ctx.stroke();

            // Rysuj kola
            ctx.beginPath();
            ctx.arc(34 + 1.5, 46 - 15, 4, 0, 2 * Math.PI);
            ctx.fillStyle = "black";
            ctx.fill();
            ctx.stroke();

            ctx.beginPath();
            ctx.arc(34 + 1.5, 46 - 15, 1, 0, 2 * Math.PI);
            ctx.fillStyle = "white";
            ctx.fill();
            ctx.stroke();

            ctx.beginPath();
            ctx.arc(10 + 1.5, 46 - 15, 4, 0, 2 * Math.PI);
            ctx.fillStyle = "black";
            ctx.fill();
            ctx.stroke();

            ctx.beginPath();
            ctx.arc(10 + 1.5, 46 - 15, 1, 0, 2 * Math.PI);
            ctx.fillStyle = "white";
            ctx.fill();
            ctx.stroke();
        }
    </script>

    <title>
        Sklep samochodowy
    </title>
</head>

<body onload="draw()">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous"></script>
    <script src="https://unpkg.com/react/umd/react.development.js" crossorigin=""></script>
    <script src="https://unpkg.com/react-dom/umd/react-dom.development.js" crossorigin=""></script>
    <script src="https://unpkg.com/babel-standalone/babel.min.js"></script>

    <nav class="navbar navbar-expand-lg" style="background-color: #FFC107;">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <canvas id="canvas" width="50" height="50">
                    Wygląda na to, że twoja przeglądarka nie obsługuje elementu "canvas"
                </canvas>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav">
                    <div class="dropdown">
                        <a class="btn btn-warning dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                            aria-expanded="false">
                            Samochody
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="#">Elektryczne</a></li>
                            <li><a class="dropdown-item" href="#">Spalinowe</a></li>
                        </ul>
                    </div>
                </ul>
                <form class="d-flex" role="search">
                    <input class="form-control me-2" type="search" placeholder="Szukaj" aria-label="Search">
                    <button class="btn btn-warning" type="button">Szukaj</button>
                </form>
            </div>
        </div>
    </nav>

    <main>
        <div class="d-sm-flex flex-row">
            <div class="azure flex-column" id="mercedes">
                <img src="pictures/amg-gt.jpg" alt="Tu jest mercedes">
                <div class="content">
                    <h4>Mercedes AMG-GT</h4>
                    <ul>
                        <li>Silnik V8 o pojemności 4 litrów</li>
                        <li>Moc nawet do 500 KM</li>
                    </ul>
                </div>
            </div>
            <div class=" azure flex-column" id="fiat">
                <img src="pictures/fiat500.jpg" alt="Tu jest fiat500">
                <div class="content">
                    <h4>Fiat 500</h4>
                    <ul>
                        <li>Silnik elektryczny</li>
                        <li>Zasięg 400km</li>
                    </ul>

                </div>
            </div>
        </div>

        <div class="d-sm-flex flex-row-reverse">
            <div class=" azure flex-column" id="bmw">
                <img class="right-align" src="pictures/BMW.jpg" alt="Tu jest BMW">
                <div class="content">
                    <h4>BMW</h4>
                    <ul>
                        <li>Napęd na tylną oś</li>
                        <li>W 2s do 100 km/h</li>
                    </ul>
                </div>
            </div>
            <div class="azure flex-column" id="volvo">
                <img src="pictures/volvo.jpg" alt="Tu jest Volvo">
                <div class=" content">
                    <h4>Volvo</h4>
                    <ul>
                        <li>Cichy silnik elektryczny</li>
                        <li>Zasięg 800km</li>
                    </ul>
                </div>
            </div>
        </div>

        <div id="shopContainer">
            <h2>Skorzystaj z naszej oferty!</h2>
            <form class="d-flex justify-content-center">
                <input class="form-control" type="text" id="commandLine" name="commandLine">
                <button class="btn btn-warning" type="submit">Wykonaj</button>
            </form>
        </div>

        <div id="fotter" class="d-sm-flex flex-row text-white">
            &copy;Szablony CyberAGH
        </div>
    </main>

</body>

</html>`);
    response.end();
  } else if (url.pathname === "/" && request.method === "POST") {
    /* ---------------------- */
    /* Route "POST('/')" */
    /* ---------------------- */
    const command = url.searchParams.get("command");
    const result = executeCommandOnServer(command);

    response.writeHead(200, {
      "Content-Type": "application/json; charset=utf-8",
    });
    response.write(JSON.stringify(result));
    response.end();
  } else if (url.pathname === "/submit" && request.method === "GET") {
    /* ---------------------- */
    /* Route "GET('/submit')" */
    /* ---------------------- */
    response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });

    response.write(`${url.searchParams.get("command")}`);

    response.end();
  } else {
    /* -------------------------- */
    /* If no route is implemented */
    /* -------------------------- */
    response.writeHead(501, { "Content-Type": "text/plain; charset=utf-8" });
    response.write("Error 501: Not implemented");
    response.end();
  }
}

function executeCommandOnServer(command) {
  const commandParts = command.split(" ");
  const operation = commandParts[0].toLowerCase();

  switch (operation) {
    case "sell":
      return sellProductOnServer(commandParts);
    case "displaycustomers":
      return { result: displayCustomersOnServer() };
    case "displaypurchasehistory":
      return displayPurchaseHistoryOnServer(commandParts);
    case "displayinventory":
      return { result: displayInventoryOnServer() };
    case "addcustomer":
      return addCustomerOnServer(commandParts);
    case "showproductdetails":
      return showProductDetailsOnServer(commandParts);
    default:
      return { result: `Nieznana operacja: ${operation}` };
  }
}

function sellProductOnServer(commandParts) {
  const customerFirstName = commandParts[1];
  const customerLastName = commandParts[2];
  const productName = commandParts[3];
  const quantityToSell = parseInt(commandParts[4]);

  const customer = clientsData.find(
    (c) => c.firstName === customerFirstName && c.lastName === customerLastName
  );
  const product = productsData.find((p) => p.name === productName);

  if (customer && product && quantityToSell > 0) {
    if (product.quantity >= quantityToSell) {
      product.quantity -= quantityToSell;
      const purchaseHistory = customer.purchaseHistory || [];
      const cost = product.price * quantityToSell;
      purchaseHistory.push({
        product: { name: product.name, price: product.price },
        quantity: quantityToSell,
        date: new Date(),
        totalCost: cost,
      });
      customer.purchaseHistory = purchaseHistory;

      writeJsonFile(clientsFile, clientsData);
      writeJsonFile(productsFile, productsData);

      const successMessage = `Sold ${quantityToSell} units of "${productName}" to customer "${customerFirstName} ${customerLastName}". Total cost: ${cost}`;
      return { result: successMessage };
    } else {
      return {
        result: `Product "${productName}" is unavailable or insufficient quantity in stock.`,
      };
    }
  } else {
    return { result: "Invalid input data or negative quantity." };
  }
}

function displayCustomersOnServer() {
  const customersList = clientsData.map(
    (customer) => `${customer.firstName} ${customer.lastName}`
  );
  return `Lista klientów: ${customersList.join(", ")}`;
}

function displayPurchaseHistoryOnServer(commandParts) {
  const customerFirstName = commandParts[1];
  const customerLastName = commandParts[2];
  const customer = data.clients.find(
    (c) => c.firstName === customerFirstName && c.lastName === customerLastName
  );

  if (customer) {
    const purchaseHistory = customer.purchaseHistory || [];
    const historyDetails = purchaseHistory.map(
      (purchase) =>
        `- ${purchase.product.name}, quantity: ${purchase.quantity}, cost: ${purchase.totalCost}`
    );
    const totalCost = purchaseHistory.reduce(
      (sum, purchase) => sum + purchase.totalCost,
      0
    );

    return `Purchase history for customer "${customerFirstName} ${customerLastName}":\n${historyDetails.join(
      "\n"
    )}\nTotal purchase cost: ${totalCost}`;
  } else {
    return `Customer with name "${customerFirstName} ${customerLastName}" not found`;
  }
}

function displayInventoryOnServer() {
  const inventoryDetails = productsData.map(
    (product) => `- ${product.name}: ${product.quantity} sztuk`
  );
  return `Stan magazynu:\n${inventoryDetails.join("\n")}`;
}

function addCustomerOnServer(commandParts) {
  const firstName = commandParts[1];
  const lastName = commandParts[2];

  if (firstName && lastName) {
    const newCustomer = { firstName, lastName, purchaseHistory: [] };
    data.clients.push(newCustomer);

    return { result: `Dodano nowego klienta: ${firstName} ${lastName}` };
  } else {
    return { result: "Nieprawidłowe dane wejściowe." };
  }
}

function showProductDetailsOnServer(commandParts) {
  const productName = commandParts[1];
  const product = data.products.find((p) => p.name === productName);

  if (product) {
    return `Szczegóły produktu:\nNazwa: ${product.name}\nIlość dostępnych: ${product.quantity}\nCena: ${product.price}`;
  } else {
    return `Nie znaleziono produktu o nazwie "${productName}"`;
  }
}

/* ************************************************** */
/* Main block
/* ************************************************** */
const server = http.createServer(requestListener);
const PORT = process.env.PORT || 8000; // Use environment variable for port or default to 8000

// Start server
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
  console.log('To stop the server, press "CTRL + C"');
});
