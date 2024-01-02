const http = require("http");
const fs = require("fs");
const path = require("path");

const server = http.createServer(requestListener);
const PORT = process.env.PORT || 8000;

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

const writeLock = {};

async function writeJsonFile(filename, jsonData) {
  if (!writeLock[filename]) {
    writeLock[filename] = true;

    try {
      const data = JSON.stringify(jsonData, null, 2);

      // Opóźnienie zapisu pliku (np. 500 ms)
      await new Promise((resolve) => setTimeout(resolve, 500));

      await fs.promises.writeFile(filename, data, "utf8");
      console.log(`Data written to ${filename}`);
    } catch (error) {
      console.error(`Error writing to file ${filename}:`, error.message);
    } finally {
      writeLock[filename] = false;
    }
  } else {
    console.log(
      `Write operation for ${filename} is already in progress. Skipping...`
    );
  }
}

server.listen(PORT, () => {
  console.log(`Serwer działa na porcie ${PORT}`);
  console.log('Aby zatrzymać serwer, naciśnij "CTRL + C"');
});

function requestListener(request, response) {
  const url = new URL(request.url, `http://${request.headers.host}`);

  if (url.pathname.startsWith("/pictures/") && request.method === "GET") {
    const imageName = path.basename(url.pathname);
    const imagePath = path.join(__dirname, "pictures", imageName);

    fs.access(imagePath, fs.constants.R_OK, (err) => {
      if (err) {
        response.writeHead(404, {
          "Content-Type": "text/plain; charset=utf-8",
        });
        response.write("Not Found");
        response.end();
      } else {
        response.writeHead(200, { "Content-Type": "image/jpeg" }); // Ustaw typ zawartości w zależności od formatu obrazu
        fs.createReadStream(imagePath).pipe(response);
      }
    });
  } else if (url.pathname === "/" && request.method === "GET") {
    // Obsługa żądania GET dla ścieżki "/"
    // Wysyłamy odpowiednią zawartość HTML do klienta
    response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    const htmlContent = fs.readFileSync(
      path.join(__dirname, "index.html"),
      "utf8"
    );
    response.write(htmlContent);
    response.end();
  } else if (url.pathname === "/submit" && request.method === "GET") {
    // Obsługa żądania GET dla ścieżki "/submit"
    const command = url.searchParams.get("command");
    const result = executeCommandOnServer(command);

    response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
    response.write(result);
    response.end();
  } else {
    response.writeHead(501, { "Content-Type": "text/plain; charset=utf-8" });
    response.write("Błąd 501: Niezaimplementowane");
    response.end();
  }
}

function executeCommandOnServer(command) {
  const commandParts = command.split(" ");
  const operation = commandParts[0].toLowerCase();

  switch (operation) {
    case "sell":
      return sellProductOnServer(commandParts);
    case "showclients":
      return showClientsOnServer();
    case "showhistory":
      return showHistoryOnServer(commandParts);
    case "showwarehouse":
      return showWarehouseOnServer();
    case "addclient":
      return addClientOnServer(commandParts);
    case "showproductdetails":
      return showProductDetailsOnServer(commandParts);
    default:
      return `Nieznana operacja: ${operation}`;
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
  const productIndex = productsData.findIndex((p) => p.name === productName);

  if (customer && productIndex !== -1 && quantityToSell > 0) {
    const product = productsData[productIndex];

    if (product.quantity >= quantityToSell) {
      product.quantity -= quantityToSell;

      // Utwórz nowy obiekt historii zakupów dla każdego zakupu
      const cost = product.price * quantityToSell;
      const purchase = {
        product: { name: product.name, price: product.price },
        quantity: quantityToSell,
        date: new Date(),
        totalCost: cost,
      };

      // Sprawdź, czy istnieje tablica purchaseHistory i utwórz ją, jeśli nie
      customer.purchaseHistory = customer.purchaseHistory || [];

      // Utwórz nową tablicę historii zakupów z nowym zakupem
      customer.purchaseHistory.push(purchase);

      // Aktualizuj pliki JSON po zakupie
      //   writeJsonFile(clientsFile, clientsData);
      //   writeJsonFile(productsFile, productsData);

      const successMessage = `Sprzedano ${quantityToSell} ${productName} dla klienta ${customerFirstName} ${customerLastName}. Kosztowało to: ${cost}zł`;
      return successMessage;
    } else {
      return `Produkt ${productName} jest niedostępny albo nie można go kupić w takiej ilości.`;
    }
  } else {
    return "Nieprawidłowe dane (być może chcesz kupić ujemną ilość towaru).";
  }
}

function showClientsOnServer() {
  const customersList = clientsData.map(
    (customer) => `${customer.firstName} ${customer.lastName}`
  );
  return `Lista klientów: ${customersList.join(", ")}`;
}

function showHistoryOnServer(commandParts) {
  const customerFirstName = commandParts[1];
  const customerLastName = commandParts[2];
  const customer = clientsData.find(
    (c) => c.firstName === customerFirstName && c.lastName === customerLastName
  );

  if (customer) {
    const purchaseHistory = customer.purchaseHistory || [];
    const historyDetails = purchaseHistory.map(
      (purchase) =>
        `- ${purchase.product.name}, liczba sztuk: ${purchase.quantity}, cena: ${purchase.totalCost}zł`
    );
    const totalCost = purchaseHistory.reduce(
      (sum, purchase) => sum + purchase.totalCost,
      0
    );

    return `Historia transakcji dla klienta ${customerFirstName} ${customerLastName}:\n${historyDetails.join(
      "\n"
    )}\nWydano łącznie: ${totalCost}`;
  } else {
    return `Klienta ${customerFirstName} ${customerLastName} nie znaleziono.`;
  }
}

function showWarehouseOnServer() {
  const inventoryDetails = productsData.map(
    (product) => `- ${product.name}: ${product.quantity} sztuk`
  );
  return `Stan magazynu:\n${inventoryDetails.join("\n")}`;
}

function addClientOnServer(commandParts) {
  const firstName = commandParts[1];
  const lastName = commandParts[2];

  if (firstName && lastName) {
    const newCustomer = { firstName, lastName, purchaseHistory: [] };
    clientsData.push(newCustomer);

    return `Dodano nowego klienta: ${firstName} ${lastName}`;
  } else {
    return "Nieprawidłowe dane wejściowe.";
  }
}

function showProductDetailsOnServer(commandParts) {
  const productName = commandParts[1];
  const product = productsData.find((p) => p.name === productName);

  if (product) {
    return `Szczegóły produktu:\nNazwa: ${product.name}\nIlość dostępnych: ${product.quantity}\nCena: ${product.price}zł`;
  } else {
    return `Nie znaleziono produktu o nazwie ${productName}`;
  }
}
