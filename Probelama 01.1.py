# Importar la librería necesaria
import pandas as pd

# Leer el archivo CSV en un DataFrame
df_airbnb = pd.read_csv("./data/airbnb.csv")

# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df_airbnb.head())

# 1. Verificar las dimensiones del DataFrame (número de filas y columnas)
print("\nDimensiones del DataFrame (filas, columnas):")
print(df_airbnb.shape)

# 2. Listar las columnas del DataFrame
print("\nNombres de las columnas:")
print(df_airbnb.columns)

# 3. Verificar los tipos de datos de cada columna
print("\nTipos de datos de cada columna:")
print(df_airbnb.dtypes)

# 4. Obtener un resumen estadístico de las columnas numéricas
print("\nResumen estadístico de las columnas numéricas:")
print(df_airbnb.describe())

# 5. Verificar la existencia de valores nulos en el DataFrame
print("\nConteo de valores nulos por columna:")
print(df_airbnb.isnull().sum())

# 6. Obtener el número de valores únicos para las columnas categóricas
print("\nValores únicos en la columna 'room_type':")
print(df_airbnb['room_type'].unique())

print("\nValores únicos en la columna 'neighborhood':")
print(df_airbnb['neighborhood'].unique())

# 7. Contar la frecuencia de cada valor en las columnas categóricas
print("\nFrecuencia de cada tipo de habitación (room_type):")
print(df_airbnb['room_type'].value_counts())

print("\nFrecuencia de cada barrio (neighborhood):")
print(df_airbnb['neighborhood'].value_counts())

# 8. Análisis de la distribución de precios
print("\nDistribución de los precios:")
print(df_airbnb['price'].describe())