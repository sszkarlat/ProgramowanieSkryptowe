const express = require("express");
const router = express.Router();
const bodyParser = require("body-parser");
const { MongoClient } = require("mongodb");

const client = new MongoClient("mongodb://127.0.0.1:27017");
client.connect();
const db = client.db("warehouse");
const products = db.collection("products");

router.get("/", (req, res, next) => {
  res.status(200).render("add");
});

router.post(
  "/submit",
  bodyParser.urlencoded({ extended: true }),
  async (req, res, next) => {
    const command = req.body.commandLine;
    const result = await addNewProductToDB(command);

    res.status(200).send(result);
  }
);

async function addNewProductToDB(command) {
  const commandParts = command.split(" ");
  const productName = commandParts[0];
  const quantity = parseInt(commandParts[1]);
  const price = parseFloat(commandParts[2]);

  try {
    // Sprawdź, czy produkt o danej nazwie już istnieje
    const existingProduct = await products.findOne({ name: productName });
    if (existingProduct) {
      return `Produkt o nazwie ${productName} już istnieje w bazie danych.`;
    }

    // Dodaj nowy produkt
    const result = await products.insertOne({
      name: productName,
      quantity: quantity,
      price: price,
    });

    // Nowy produkt
    console.log(result.insertedId);
    if (result.insertedId) {
      return `Dodano nowy produkt: ${productName}.`;
    } else {
      return "Nie udało się dodać nowego produktu.";
    }
  } catch (error) {
    console.error("Error adding new product:", error);
    throw error;
  }
}

module.exports = router;
