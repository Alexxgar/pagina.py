import streamlit as st
from streamlit.components.v1 import html

# HTML, CSS y JS incrustado
html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Heladería Tropical</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      margin: 0;
      background: #fff6f6;
    }
    header {
      background-color: #f44336;
      color: white;
      padding: 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    header h1 {
      margin: 0;
    }
    .search-bar {
      padding: 1rem;
      text-align: center;
    }
    .search-bar input {
      width: 60%;
      padding: 0.5rem;
      font-size: 1rem;
    }
    .productos {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 1rem;
      padding: 1rem;
    }
    .producto {
      background: white;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      width: 250px;
      padding: 1rem;
      text-align: center;
    }
    .producto img {
      max-width: 100%;
      height: auto;
      border-radius: 8px;
    }
    .btn {
      background-color: #ff4081;
      color: white;
      border: none;
      padding: 0.5rem 1rem;
      border-radius: 5px;
      cursor: pointer;
      margin-top: 0.5rem;
    }
    .btn:hover {
      background-color: #e91e63;
    }
    footer {
      text-align: center;
      padding: 1rem;
      background: #f8dcdc;
    }
  </style>
</head>
<body>

  <header>
    <h1>🍦 Heladería Tropical</h1>
    <div id="carrito">🛒 Carrito (0)</div>
  </header>

  <div class="search-bar">
    <input type="text" placeholder="Buscar helado..." onkeyup="buscarHelado(this.value)">
  </div>

  <div class="productos" id="lista-productos">
    <!-- Productos se insertan por JavaScript -->
  </div>

  <footer>
    © 2025 Heladería Tropical. Todos los derechos reservados.
  </footer>

  <script>
    const productos = [
      {
        nombre: "MegaCono Clásico",
        precio: 3500,
        imagen: "https://www.tiendacremhelado.com.co/wp-content/uploads/2021/04/cono-megacono.png"
      },
      {
        nombre: "Mini Cono Vainilla",
        precio: 2500,
        imagen: "https://www.tiendacremhelado.com.co/wp-content/uploads/2021/04/cono-mini-vainilla.png"
      },
      {
        nombre: "Sandwich Cremoso",
        precio: 3700,
        imagen: "https://www.tiendacremhelado.com.co/wp-content/uploads/2021/04/sandwich-cremoso.png"
      }
    ];

    let carrito = [];

    function renderProductos(filtro = "") {
      const contenedor = document.getElementById("lista-productos");
      contenedor.innerHTML = "";

      const filtrados = productos.filter(p =>
        p.nombre.toLowerCase().includes(filtro.toLowerCase())
      );

      filtrados.forEach(p => {
        const div = document.createElement("div");
        div.className = "producto";
        div.innerHTML = `
          <img src="${p.imagen}" alt="${p.nombre}" />
          <h3>${p.nombre}</h3>
          <p>Precio: $${p.precio}</p>
          <button class="btn" onclick='agregarAlCarrito("${p.nombre}")'>Agregar</button>
        `;
        contenedor.appendChild(div);
      });
    }

    function agregarAlCarrito(nombre) {
      carrito.push(nombre);
      document.getElementById("carrito").innerText = `🛒 Carrito (${carrito.length})`;
    }

    function buscarHelado(valor) {
      renderProductos(valor);
    }

    renderProductos();
  </script>

</body>
</html>
"""

# Mostrar en Streamlit
st.set_page_config(layout="wide")
st.title("Vista HTML de la Heladería")
html(html_code, height=900, scrolling=True)
