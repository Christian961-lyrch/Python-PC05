import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df_airbnb = pd.read_csv("./data/airbnb.csv")

# Agrupamiento 1: Precio promedio por tipo de propiedad
precio_promedio_por_tipo = df_airbnb.groupby('room_type')['price'].mean().reset_index()

# Graficar el precio promedio por tipo de propiedad
plt.figure(figsize=(8, 6))
sns.barplot(x='room_type', y='price', data=precio_promedio_por_tipo, palette='viridis')
plt.title('Precio Promedio por Tipo de Propiedad')
plt.xlabel('Tipo de Propiedad')
plt.ylabel('Precio Promedio (€)')
plt.show()

# Agrupamiento 2: Número de propiedades por barrio
numero_propiedades_por_barrio = df_airbnb.groupby('neighborhood').size().reset_index(name='counts')

# Graficar el número de propiedades por barrio
plt.figure(figsize=(12, 8))
sns.barplot(x='counts', y='neighborhood', data=numero_propiedades_por_barrio.sort_values('counts', ascending=False), palette='plasma')
plt.title('Número de Propiedades por Barrio en Lisboa')
plt.xlabel('Número de Propiedades')
plt.ylabel('Barrio')
plt.show()