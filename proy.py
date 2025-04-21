import streamlit as st

st.set_page_config(page_title="Tienda de Helados", layout="wide")

# Simular base de productos
productos = [
    {"nombre": "Galleta con Helado Jumbo", "precio": 3700, "imagen": "3221d579-f43a-40a8-8f0e-938eced09aaf.png"},
    {"nombre": "Paleta Aloha Limón", "precio": 2000, "imagen": "71fb1ed8-ae04-4b03-974e-fead72370140.png"},
    {"nombre": "Postre de Limón", "precio": 3200, "imagen": "09a3b333-432b-429f-8685-27333d6d60a7.png"},
]

# Carrito en sesión
if "carrito" not in st.session_state:
    st.session_state.carrito = []

st.title("🍦 Tienda de Helados")

cols = st.columns(len(productos))

# Mostrar productos
for i, producto in enumerate(productos):
    with cols[i]:
        st.image(f"./{producto['imagen']}", width=200)
        st.subheader(producto["nombre"])
        st.write(f"Precio: ${producto['precio']}")
        if st.button(f"Agregar {i}", key=i):
            st.session_state.carrito.append(producto)

st.divider()
st.header("🛒 Carrito de Compras")

if st.session_state.carrito:
    total = 0
    for item in st.session_state.carrito:
        st.write(f"- {item['nombre']} - ${item['precio']}")
        total += item["precio"]
    st.markdown(f"### Total: ${total}")
else:
    st.write("Tu carrito está vacío.")
