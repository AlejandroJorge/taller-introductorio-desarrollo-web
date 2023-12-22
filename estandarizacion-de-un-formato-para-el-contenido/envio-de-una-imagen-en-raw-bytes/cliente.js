const { write, writeFileSync } = require("fs");

const PORT = 5000;

const response = fetch(`http://localhost:${PORT}`);

response.then(async (value) => {
  const rawBytes = (await value.body.getReader().read()).value;
  writeFileSync("data-cliente/imagen.jpg", rawBytes);
});
