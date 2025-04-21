import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Heladería Tropical", layout="wide")

st.sidebar.title("Carrito de Compras")

# Inicializar el carrito en la sesión si no existe
if "carrito" not in st.session_state:
    st.session_state.carrito = []

# Lista de productos (con imágenes reales de la web oficial)
productos = [
    {
        "nombre": "MegaCono Clásico",
        "precio": 3500,
        "categoria": "Conos",
        "imagen": "https://www.tiendacremhelado.com.co/wp-content/uploads/2021/04/cono-megacono.png"
    },
    {
        "nombre": "Mini Cono Vainilla",
        "precio": 2500,
        "categoria": "Conos",
        "imagen": "https://www.tiendacremhelado.com.co/wp-content/uploads/2021/04/cono-mini-vainilla.png"
    },
    {
        "nombre": "Sandwich Cremoso",
        "precio": 3700,
        "categoria": "Sandwiches",
        "imagen": "https://www.tiendacremhelado.com.co/wp-content/uploads/2021/04/sandwich-cremoso.png"
    }
]

# Función para agregar producto al carrito
def agregar_al_carrito(producto):
    st.session_state.carrito.append(producto)

# Mostrar productos en el carrito
if st.session_state.carrito:
    total = sum(item["precio"] for item in st.session_state.carrito)
    for item in st.session_state.carrito:
        st.sidebar.write(f"{item['nombre']} - ${item['precio']}")
    st.sidebar.write(f"**Total: ${total}**")
    if st.sidebar.button("Vaciar carrito"):
        st.session_state.carrito = []
else:
    st.sidebar.write("Tu carrito está vacío.")

# Encabezado principal
st.title("Heladería Tropical")
st.write("¡Explora nuestros sabores irresistibles y arma tu carrito!")

# Filtro por categoría
categorias = ["Todos"] + sorted(list(set(p["categoria"] for p in productos)))
categoria_seleccionada = st.selectbox("Filtrar por categoría", categorias)

# Buscador
busqueda = st.text_input("Buscar helado...")

# Filtrar productos según búsqueda y categoría
productos_filtrados = [
    p for p in productos
    if (categoria_seleccionada == "Todos" or p["categoria"] == categoria_seleccionada)
    and (busqueda.lower() in p["nombre"].lower())
]

# Mostrar productos
cols = st.columns(3)

for idx, producto in enumerate(productos_filtrados):
    with cols[idx % 3]:
        st.image(producto["imagen"], caption=producto["nombre"], use_container_width=True)
        st.write(f"**{producto['nombre']}**")
        st.write(f"Precio: ${producto['precio']}")
        if st.button(f"Agregar al carrito {producto['nombre']}", key=producto['nombre']):
            agregar_al_carrito(producto)
