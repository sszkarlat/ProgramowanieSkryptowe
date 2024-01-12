// routes/client.js

const express = require("express");
const router = express.Router();
const bodyParser = require("body-parser");
const { MongoClient } = require("mongodb");

const client = new MongoClient("mongodb://127.0.0.1:27017");
client.connect();
const db = client.db("warehouse");
const clientsCollection = db.collection("clients");
const productsCollection = db.collection("products");

router.get("/", (req, res, next) => {
  res.status(200).render("submit");
});

router.get("/getProductData/:productName", async (req, res, next) => {
  const productName = req.params.productName;
  try {
    const productData = await getProductData(productName);
    res.status(200).json(productData);
  } catch (error) {
    console.error("Error fetching product data:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

async function getProductData(productName) {
  // Modify this function based on your actual data structure
  // For demonstration purposes, assuming a simple product structure
  const product = {
    productName: productName,
    value: 50000, // Replace with the actual value from your database
  };

  return product;
}

module.exports = router;

router.post("/getProductData/:productName", async (req, res, next) => {
  const productName = req.params.productName;
  try {
    const productData = await getProductData(productName);
    res.status(200).json(productData);
  } catch (error) {
    console.error("Error fetching product data:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});


module.exports = router;
