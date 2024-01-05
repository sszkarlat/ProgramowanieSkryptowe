// Wersja 1.
// var http = require("http");

// function requestListener (request, response) {
//     console.log("A request from client has appeared");
//     response.writeHead(200, {"Content-Type": "text/plain"});
//     response.write("Hello World!");
//     response.end();
// }

// Wersja 2.
const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const port = 8080;

app.get("/form", (req, res) => {
  res.status(200).send(`
        <form method="POST" action="/submit">
            <input name="login" value="Jan">
            <input name="password" value="Kowalski (Nowak) ąę">
            <input type="submit">
        </form>
    `);
});

app.post("/submit", bodyParser.urlencoded({ extended: true }), (req, res) => {
  const login = req.body.login;
  const password = req.body.password;

  res.status(200).send(`${login}\n${password}\n`);
  console.log("Wykonało się");
});

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
