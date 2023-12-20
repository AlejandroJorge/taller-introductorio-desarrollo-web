const url = "http://localhost:5000";

const req_data = {
  cadena: "Hola mundo. Esto es una prueba.",
};

fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(req_data),
})
  .then((res) => res.json())
  .then((res) => console.log(res));
