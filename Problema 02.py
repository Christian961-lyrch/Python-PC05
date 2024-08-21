#Problema 02. 


import pandas as pd
import sqlite3
from pymongo import MongoClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Cargar los datos
df = pd.read_csv("winemag-data-130k-v2.csv")

# Exploración básica del DataFrame
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

# Renombrar columnas
df.rename(columns={
    'country': 'Country',
    'points': 'Score',
    'price': 'Price',
    'variety': 'Variety',
}, inplace=True)

# Crear nuevas columnas
# 1. Categoría de Precio
df['Price_Category'] = pd.cut(df['Price'], bins=[0, 20, 50, 100, 200, 1000], labels=['Low', 'Medium', 'High', 'Very High', 'Luxury'])

# 2. Continent based on country
continent_map = {
    'US': 'North America', 'France': 'Europe', 'Italy': 'Europe', 'Spain': 'Europe',
    'Chile': 'South America', 'Argentina': 'South America', 'Australia': 'Oceania',
    'South Africa': 'Africa', 'Germany': 'Europe', 'Portugal': 'Europe'
}
df['Continent'] = df['Country'].map(continent_map)

# 3. High Score Flag
df['High_Score'] = df['Score'] >= 90

# 4. Price per Point
df['Price_per_Point'] = df['Price'] / df['Score']

# Reporte 1: Promedio de precio y cantidad de reviews por país, ordenado por precio promedio descendente
reporte1 = df.groupby('Country').agg(
    Avg_Price=('Price', 'mean'),
    Num_Reviews=('Score', 'count')
).sort_values(by='Avg_Price', ascending=False)

# Reporte 2: Los 10 vinos con mejor puntuación por continente
reporte2 = df.sort_values(by='Score', ascending=False).groupby('Continent').head(10)

# Reporte 3: Cantidad de vinos por categoría de precio y continente
reporte3 = df.groupby(['Continent', 'Price_Category']).size().unstack().fillna(0)

# Reporte 4: Promedio de precio por variedad de vino, ordenado por precio promedio
reporte4 = df.groupby('Variety').agg(
    Avg_Price=('Price', 'mean')
).sort_values(by='Avg_Price', ascending=False)

# Exportar los reportes a diferentes formatos
reporte1.to_csv("reporte1.csv")
reporte2.to_excel("reporte2.xlsx")
conn = sqlite3.connect('reporte3.db')
reporte3.to_sql('reporte3', conn, if_exists='replace')
conn.close()

client = MongoClient('mongodb://localhost:27017/')
db = client['wine_db']
collection = db['reporte4']
collection.insert_many(reporte4.reset_index().to_dict(orient='records'))

# Enviar el reporte por correo electrónico
def enviar_reporte_por_email(archivo, destinatario):
    remitente = 'tu_correo@example.com'
    asunto = 'Reporte de Vinos'
    cuerpo = 'Adjunto el reporte solicitado.'
    password = 'tu_contraseña'

    # Crear el mensaje de correo
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Adjuntar el archivo
    with open(archivo, 'rb') as adjunto:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(adjunto.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={archivo}')
        mensaje.attach(parte)

    # Enviar el correo
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remitente, password)
    texto = mensaje.as_string()
    servidor.sendmail(remitente, destinatario, texto)
    servidor.quit()

# Enviar reporte1.csv por correo
enviar_reporte_por_email("reporte1.csv", "destinatario@example.com")