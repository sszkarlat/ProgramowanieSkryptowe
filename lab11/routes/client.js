const express = require("express");
const router = express.Router();
const bodyParser = require("body-parser");
const { MongoClient } = require("mongodb");

const client = new MongoClient("mongodb://127.0.0.1:27017");
client.connect();
const db = client.db("warehouse");
const clients = db.collection("clients");
const products = db.collection("products");

router.get("/", (req, res, next) => {
  res.status(200).render("submit");
});

router.post(
  "/submit",
  bodyParser.urlencoded({ extended: true }),
  async (req, res, next) => {
    const command = req.body.commandLine;
    const result = await executeCommandOnServer(command);

    res.status(200).send(result);
  }
);

async function executeCommandOnServer(command) {
  await client.connect();
  const db = client.db("warehouse");

  const commandParts = command.split(" ");
  const operation = commandParts[0].toLowerCase();
  let result;

  switch (operation) {
    case "sell":
      result = await sellProductOnServer(commandParts);
      break;
    case "showclients":
      result = await showClientsOnServer();
      break;
    case "showhistory":
      result = await showHistoryOnServer(commandParts);
      break;
    case "showwarehouse":
      result = await showWarehouseOnServer();
      break;
    case "showproductdetails":
      result = await showProductDetailsOnServer(commandParts);
      break;
    default:
      result = `Nieznana operacja: ${operation}`;
  }

  client.close();
  return result;
}

async function showWarehouseOnServer() {
  try {
    const warehouseProducts = await products.find().toArray();

    if (warehouseProducts.length > 0) {
      const inventoryDetails = warehouseProducts.map(
        (product) => `- ${product.name}: ${product.quantity} sztuk`
      );
      return `Stan magazynu:\n${inventoryDetails.join("\n")}`;
    } else {
      return "Magazyn jest pusty.";
    }
  } catch (error) {
    console.error("Error fetching products:", error);
    throw error;
  }
}

async function sellProductOnServer(commandParts) {
  const customerFirstName = commandParts[1];
  const customerLastName = commandParts[2];
  const productName = commandParts[3];
  const quantityToSell = parseInt(commandParts[4]);

  const customer = await clients.findOne({
    firstName: customerFirstName,
    lastName: customerLastName,
  });

  const product = await products.findOne({ name: productName });

  if (customer && product && quantityToSell > 0) {
    const result = await products.updateOne(
      { name: productName, quantity: { $gte: quantityToSell } },
      { $inc: { quantity: -quantityToSell } }
    );

    if (result.modifiedCount > 0) {
      const cost = product.price * quantityToSell;
      const purchase = {
        product: { name: product.name, price: product.price },
        quantity: quantityToSell,
        date: new Date(),
        totalCost: cost,
      };

      await clients.updateOne(
        { firstName: customerFirstName, lastName: customerLastName },
        { $push: { purchaseHistory: purchase } }
      );

      const successMessage = `Sprzedano ${quantityToSell} ${productName} dla klienta ${customerFirstName} ${customerLastName}. Kosztowało to: ${cost}zł`;
      return successMessage;
    } else {
      return `Produkt ${productName} jest niedostępny albo nie można go kupić w takiej ilości.`;
    }
  } else {
    return "Nieprawidłowe dane (być może chcesz kupić ujemną ilość towaru).";
  }
}

async function showClientsOnServer() {
  try {
    const clientsList = await clients.find().toArray();

    if (clientsList.length > 0) {
      const customersDetails = clientsList.map(
        (customer) => `${customer.firstName} ${customer.lastName}`
      );
      return `Lista klientów: ${customersDetails.join(", ")}`;
    } else {
      return "Brak klientów w bazie danych.";
    }
  } catch (error) {
    console.error("Error fetching clients:", error);
    throw error;
  }
}

async function showHistoryOnServer(commandParts) {
  const customerFirstName = commandParts[1];
  const customerLastName = commandParts[2];

  try {
    const customer = await clients.findOne({
      firstName: customerFirstName,
      lastName: customerLastName,
    });

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
  } catch (error) {
    console.error("Error fetching purchase history:", error);
    throw error;
  }
}

async function showProductDetailsOnServer(commandParts) {
  const productName = commandParts[1];

  try {
    const product = await products.findOne({ name: productName });

    if (product) {
      return `Szczegóły produktu:\nNazwa: ${product.name}\nIlość dostępnych: ${product.quantity}\nCena: ${product.price}zł`;
    } else {
      return `Nie znaleziono produktu o nazwie ${productName}`;
    }
  } catch (error) {
    console.error("Error fetching product details:", error);
    throw error;
  }
}

module.exports = router;
