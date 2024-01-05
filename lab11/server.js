const express = require("express");
const morgan = require("morgan");
const clientRouter = require("./routes/client");
const adminRouter = require("./routes/admin");

const app = express();
const port = 8000;
app.locals.pretty = app.get("env") === "development"; // The resulting HTML code will be indented in the development environment
app.use(morgan("dev"));

app.set("view engine", "pug");
app.use(express.static("public"));
app.use("/client", clientRouter);
app.use("/admin", adminRouter);

app.get("/", (req, res) => {
  res.status(200).render("index");
});

app.listen(port, () => {
  console.log("The server was started on port 8000");
  console.log('To stop the server, press "CTRL + C"');
});
