import pandas as pd

# Supongamos que ya hemos cargado el DataFrame `df_airbnb` con todos los datos

# IDs de las propiedades de Roberto y Clara
id_roberto = 97503
id_clara = 90387

# Filtrar las propiedades por ID
propiedades_roberto_clara = df_airbnb[(df_airbnb['room_id'] == id_roberto) | (df_airbnb['room_id'] == id_clara)]

# Mostrar las propiedades de Roberto y Clara
print("Propiedades de Roberto y Clara:")
print(propiedades_roberto_clara[['room_id', 'host_id', 'neighborhood', 'reviews', 'overall_satisfaction', 'price']])

# Guardar el DataFrame en un archivo Excel
propiedades_roberto_clara.to_excel("roberto.xls", index=False)

print("El archivo 'roberto.xls' ha sido creado con éxito.")