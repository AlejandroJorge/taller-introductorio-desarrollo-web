const express = require("express");

const PORT = 5000;

const app = express();

app.get("/", (req, res) => {
  console.log("El servidor ha recibido una peticion GET en la ruta '/'");
  res.send("Hola, soy un mensaje enviado desde el servidor en la ruta '/'");
});

app.get("/gatos", (req, res) => {
  console.log("El servidor ha recibido una peticion GET en la ruta '/gatos'");
  res.send(
    "Hola, soy un mensaje enviado desde el servidor en la ruta '/gatos'"
  );
});

app.get("/perros", (req, res) => {
  console.log("El servidor ha recibido una peticion GET en la ruta '/perros'");
  res.send(
    "Hola, soy un mensaje enviado desde el servidor en la ruta '/perros'"
  );
});

app.listen(PORT, () => console.log(`Listening on http://localhost:${PORT}`));
