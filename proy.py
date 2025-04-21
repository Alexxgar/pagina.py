import streamlit as st


# Configuración de la página
st.set_page_config(page_title="Heladería Tropical", layout="wide")
st.title("Heladería Tropical")
st.markdown("¡Explora nuestros sabores irresistibles y arma tu carrito!")

# Estado del carrito
if "carrito" not in st.session_state:
    st.session_state.carrito = []

# Lista de productos
helados = [
    {
        "nombre": "MegaCono Clásico",
        "precio": 4500,
        "categoria": "Conos",
        "imagen": "https://cdn.tiendacremhelado.com.co/images/products/7702011107683-1.jpg"
    },
    {
        "nombre": "Mini Cono Vainilla",
        "precio": 2900,
        "categoria": "Conos",
        "imagen": "https://cdn.tiendacremhelado.com.co/images/products/7702011116562-1.jpg"
    },
    {
        "nombre": "Sandwich Cremoso",
        "precio": 3700,
        "categoria": "Sandwich",
        "imagen": "https://cdn.tiendacremhelado.com.co/images/products/7702011122488-1.jpg"
    },
    {
        "nombre": "Paleta Tricolor",
        "precio": 3100,
        "categoria": "Paletas",
        "imagen": "https://cdn.tiendacremhelado.com.co/images/products/7702011117552-1.jpg"
    },
    {
        "nombre": "Tarrina de Chocolate",
        "precio": 6200,
        "categoria": "Tarrinas",
        "imagen": "https://cdn.tiendacremhelado.com.co/images/products/7702011126813-1.jpg"
    },
    {
        "nombre": "Copa de Frutas",
        "precio": 5400,
        "categoria": "Copas",
        "imagen": "https://cdn.tiendacremhelado.com.co/images/products/7702011118917-1.jpg"
    },
]

# Filtro de categoría
categorias = ["Todos"] + sorted(list(set(h["categoria"] for h in helados)))
categoria_seleccionada = st.selectbox("Filtrar por categoría", categorias)

# Buscador
busqueda = st.text_input("Buscar helado...").lower()

# Filtrar productos
productos = [
    h for h in helados
    if (categoria_seleccionada == "Todos" or h["categoria"] == categoria_seleccionada)
    and (busqueda in h["nombre"].lower())
]

# Mostrar productos
for i in range(0, len(productos), 3):
    cols = st.columns(3)
    for idx, col in enumerate(cols):
        if i + idx < len(productos):
            h = productos[i + idx]
            with col:
                st.image(h["imagen"], use_column_width=True)
                st.subheader(h["nombre"])
                st.markdown(f"**Precio:** ${h['precio']}")
                if st.button("Añadir al carrito", key=h["nombre"]):
                    st.session_state.carrito.append(h)

# Carrito en la barra lateral
st.sidebar.header("Carrito de Compras")
total = 0
for item in st.session_state.carrito:
    st.sidebar.write(f"{item['nombre']} - ${item['precio']}")
    total += item["precio"]

st.sidebar.markdown(f"**Total: ${total}**")
if st.sidebar.button("Vaciar carrito"):
    st.session_state.carrito.clear()
