const express = require("express");
const path = require("path");

const PORT = 5000;

const app = express();

app.get("/", (req, res) => {
  res.sendFile("data-servidor/imagen.jpg", { root: "./" });
});

app.listen(PORT);
