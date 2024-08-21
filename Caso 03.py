import pandas as pd

# Supongamos que ya hemos cargado el DataFrame `df_airbnb` con todos los datos

# Filtrar propiedades dentro del presupuesto de Diana
presupuesto_max = 50
propiedades_dentro_presupuesto = df_airbnb[df_airbnb['price'] <= presupuesto_max]

# Dar preferencia a habitaciones compartidas y ordenar por puntuación
propiedades_dentro_presupuesto = propiedades_dentro_presupuesto.sort_values(
    by=['room_type', 'overall_satisfaction', 'price'],
    ascending=[True, False, True]
)

# Seleccionar las 10 propiedades más baratas
propiedades_seleccionadas = propiedades_dentro_presupuesto.head(10)