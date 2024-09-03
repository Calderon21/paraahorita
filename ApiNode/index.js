const express = require('express');
const app = express();
const port = 3000;

// Endpoint 1: Verificación de estado
app.get('/check', (req, res) => {
  res.status(200).send('API #1 ');
});

// Endpoint 2: Retornar JSON
app.get('/', (req, res) => {
  res.json({
    "Instancia": "Instancia #1 - API #1",
    "Curso": "Seminario de Sistemas I",
    "Seccion": "Sección A",
    "Periodo": "2do Semestre 2024",
    "Estudiante": "Denis Augusto Coronado Calderón - 202101499"
  });
});

app.listen(port, () => {
  console.log(`API #1 listening at http://localhost:${port}`);
});