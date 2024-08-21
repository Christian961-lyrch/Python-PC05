# Filtrar las propiedades según los requisitos de Alicia
filtrado_alicia = df_airbnb[
    (df_airbnb['bedrooms'] >= 2) &
    (df_airbnb['reviews'] > 10) &
    (df_airbnb['overall_satisfaction'] > 4)
]

# Ordenar por puntuación de satisfacción (de mayor a menor) y por número de críticas (de mayor a menor)
filtrado_alicia = filtrado_alicia.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False])

# Seleccionar las 3 mejores alternativas
mejores_opciones_alicia = filtrado_alicia.head(3)

# Mostrar las 3 alternativas para Alicia
print("Las 3 mejores opciones para Alicia son:")
print(mejores_opciones_alicia[['room_id', 'neighborhood', 'bedrooms', 'price', 'reviews', 'overall_satisfaction']])