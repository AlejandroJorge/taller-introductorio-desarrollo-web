const express = require("express"); // Express es una libreria para manejar servidores http de forma mas sencilla
const bodyParser = require("body-parser");

function handleTransaction(req, res) {
  const receivedData = req.body;

  cadena = receivedData.cadena;

  let caracteres = 0;
  let espacios = 0;
  let puntos = 0;

  for (const caracter of cadena) {
    if (caracter === " ") {
      espacios++;
    } else if (caracter === ".") {
      puntos++;
    }
    caracteres++;
  }

  res.json({
    caracteres: caracteres,
    espacios: espacios,
    puntos: puntos,
  });
}

const PORT = 5000;

const app = express();

app.use(bodyParser.json());

app.post("/", handleTransaction);

app.listen(PORT);
