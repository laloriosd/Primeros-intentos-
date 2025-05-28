import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Encabezado principal
st.header('📊 Ejemplos personalizados con st.write()')

# Example 1: Texto formateado con markdown
st.write('Hola, *usuario de ciencia de datos*! 🤓 Bienvenido a esta demo.')

# Example 2: Mostrar un número
st.write('Este es un número aleatorio:', np.random.randint(1000))

# Example 3: Mostrar un DataFrame personalizado
df = pd.DataFrame({
    'Producto': ['A', 'B', 'C', 'D'],
    'Precio ($)': [120, 230, 90, 160],
    'Stock': [30, 12, 45, 22]
})
st.write('📦 Inventario actual de productos:')
st.write(df)

# Example 4: Mostrar múltiples elementos
st.write('A continuación, una tabla y su resumen estadístico:', df.describe(), '👉 Datos de inventario arriba.')

# Example 5: Gráfico con Altair
df_graf = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
chart = alt.Chart(df_graf).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
).interactive()

st.write('🎯 Visualización interactiva de datos aleatorios:')
st.write(chart)

