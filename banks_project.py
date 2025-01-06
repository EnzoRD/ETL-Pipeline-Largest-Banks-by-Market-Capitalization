import datetime

def log_progress(message):
    with open('code_log.txt', 'a') as log_file:
        log_file.write(f"{datetime.datetime.now()} : {message}\n")

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(url, table_attribs):
    try:
        # Realiza la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la solicitud falla
        
        # Analiza el contenido HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encuentra la tabla con los atributos especificados
        table = soup.find('table', table_attribs)
        if table is None:
            raise ValueError("No se encontró una tabla con los atributos especificados.")
        
        # Convierte la tabla HTML en un DataFrame
        df = pd.read_html(str(table))[0]
        
        # Limpia y devuelve el DataFrame
        df.columns = df.columns.str.strip()  # Elimina espacios en los nombres de las columnas
        return df

    except Exception as e:
        print(f"Error en la función extract: {e}")
        return None


import pandas as pd
import numpy as np
import os

def transform(df, csv_path):

    try:
        # Leer el archivo CSV y convertirlo a un diccionario
        exchange_rate_df = pd.read_csv(csv_path)
        exchange_rate = exchange_rate_df.set_index('Currency')['Rate'].to_dict()

        # Crear nuevas columnas basadas en los tipos de cambio
        df['MC_GBP_Billion'] = [np.round(x * exchange_rate['GBP'], 2) for x in df['Market cap (US$ billion)']]
        df['MC_EUR_Billion'] = [np.round(x * exchange_rate['EUR'], 2) for x in df['Market cap (US$ billion)']]
        df['MC_INR_Billion'] = [np.round(x * exchange_rate['INR'], 2) for x in df['Market cap (US$ billion)']]

        return df

    except Exception as e:
        print(f"Error en la función transform: {e}")
        return None


def load_to_csv(df, output_path):
    df.to_csv(output_path, index=False)

import sqlite3

def load_to_db(df, db_name, table_name):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

def run_queries(db_name):
    conn = sqlite3.connect(db_name)
    queries = [
        "SELECT * FROM Largest_banks",
        "SELECT AVG(MC_GBP_Billion) FROM Largest_banks",
        "SELECT `Bank name` FROM Largest_banks LIMIT 5"
    ]
    for query in queries:
        print(f"Query: {query}")
        print(pd.read_sql_query(query, conn))
    conn.close()

if __name__ == "__main__":
    log_progress("Preliminares completos. Iniciando proceso ETL")
    url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
    table_attribs = {'class': 'wikitable'}  # Cambiar según la estructura de la página
    csv_path = r"C:\Users\enzor\Desktop\IBM course\Proyecto ETL python\exchange_rate.csv"

    output_csv = "./Largest_banks_data.csv"
    db_name = "Banks.db"
    table_name = "Largest_banks"
df = extract(url, table_attribs)

df = transform(df, csv_path)
print(df)



"""
    # Extracción
    df = extract(url, table_attribs)
    print(df)
    log_progress("Extracción de datos completa. Iniciando proceso de transformación")

    # Transformación
    df = transform(df, csv_path)
    log_progress("Transformación de datos completa. Iniciando proceso de carga")

    # Carga a CSV
    load_to_csv(df, output_csv)
    log_progress("Datos guardados en el archivo CSV")

    # Carga a base de datos
    load_to_db(df, db_name, table_name)
    log_progress("Datos cargados en la base de datos como una tabla, ejecutando consultas")

    # Consultas
    run_queries(db_name)
    log_progress("Proceso completo")
"""