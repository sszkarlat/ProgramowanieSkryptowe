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


const http = require("http");
const fs = require("fs");
const url = require("url");

let clients = [];
let products = [];

function readJsonFile(filePath) {
  try {
    const data = fs.readFileSync(filePath, "utf8");
    return JSON.parse(data);
  } catch (error) {
    console.error(`Błąd podczas odczytu pliku ${filePath}:`, error);
    return [];
  }
}

function writeJsonFile(filePath, data) {
  try {
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2), "utf8");
    console.log(`Zapisano dane do pliku ${filePath}`);
  } catch (error) {
    console.error(`Błąd podczas zapisu do pliku ${filePath}:`, error);
  }
}

function initializeData() {
  clients = readJsonFile("clients.json");
  products = readJsonFile("products.json");
  console.log("Zainicjalizowano dane klientów:", clients);
  console.log("Zainicjalizowano dane produktów:", products);
}

function handleRequest(req, res) {
  const parsedUrl = url.parse(req.url, true);

  if (req.method === "GET") {
    if (parsedUrl.pathname === "/clients") {
      res.writeHead(200, { "Content-Type": "application/json; charset=utf-8" });
      res.end(JSON.stringify(clients));
    } else if (parsedUrl.pathname === "/products") {
      res.writeHead(200, { "Content-Type": "application/json; charset=utf-8" });
      res.end(JSON.stringify(products));
    } else {
      res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
      res.end("Not Found");
    }
  } else if (req.method === "POST" && parsedUrl.pathname === "/sell") {
    let body = "";
    req.on("data", (chunk) => {
      body += chunk.toString();
    });

    req.on("end", () => {
      const sellData = JSON.parse(body);
      sellProduct(sellData);
      res.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
      res.end("Sale successful");
    });
  } else {
    res.writeHead(501, { "Content-Type": "text/plain; charset=utf-8" });
    res.end("Not Implemented");
  }
}

function sellProduct(sellData) {
  const { customerFirstName, customerLastName, productName, quantityToSell } =
    sellData;
  const product = products.find((p) => p.name === productName);
  const customer = clients.find((c) => c.lastName === customerLastName);

  if (
    quantityToSell > 0 &&
    product &&
    product.quantity >= quantityToSell &&
    customer
  ) {
    product.quantity -= quantityToSell;

    const purchaseHistory = customer.purchaseHistory || [];
    purchaseHistory.push({
      product: product,
      quantity: quantityToSell,
      date: new Date(),
    });
    customer.purchaseHistory = purchaseHistory;

    writeJsonFile("products.json", products);
    writeJsonFile("clients.json", clients);

    console.group("Sprzedaż");
    console.log(
      `Sprzedano ${quantityToSell} sztuk produktu "${productName}" klientowi "${customerFirstName} ${customerLastName}"`
    );
    console.groupEnd();
  } else {
    console.warn(
      `Produkt "${productName}" niedostępny lub brak wystarczającej ilości w magazynie lub nie znaleziono klienta.`
    );
  }
}

const server = http.createServer((req, res) => {
  initializeData();
  handleRequest(req, res);
});

const PORT = 8000;
server.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});
