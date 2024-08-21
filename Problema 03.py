# Problema 03. 


# Descargar el archivo
with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(zip_file_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

# 2. Descomprimir el archivo .zip
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    extract_dir = "youtube_data"
    zip_ref.extractall(extract_dir)

# 3. Leer uno de los archivos en la carpeta descomprimida
file_to_read = os.path.join(extract_dir, "000000_0.txt")
df = pd.read_csv(file_to_read, sep='\t', header=None)

# 4. Asignar nombres de columnas
df.columns = ["VideoID", "Uploader", "Age", "Category", "Length", "Views", "Rate", "Ratings", "Comments", "RelatedIDs"]

# 5. Seleccionar las columnas relevantes
df_filtered = df[["VideoID", "Age", "Category", "Views", "Rate"]]

# 6. Realizar un filtrado básico (ejemplo: seleccionar categorías específicas)
categories_to_include = ["Music", "Entertainment"]
df_filtered = df_filtered[df_filtered["Category"].isin(categories_to_include)]

# 7. Procesar los datos en MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['youtube_db']
collection = db['videos']
collection.insert_many(df_filtered.to_dict("records"))

# 8. Crear gráficos

# Gráfico 1: Distribución de vistas por categoría
plt.figure(figsize=(10, 6))
sns.boxplot(x="Category", y="Views", data=df_filtered)
plt.title("Distribución de Vistas por Categoría")
plt.xticks(rotation=45)
plt.savefig("views_by_category.png")
plt.show()

# Gráfico 2: Relación entre edad y calificación
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Age", y="Rate", hue="Category", data=df_filtered)
plt.title("Relación entre Edad y Calificación")
plt.savefig("age_vs_rate.png")
plt.show()

# 9. Compartir el link de los datos
print(f"Los datos originales se pueden encontrar en: {url}")