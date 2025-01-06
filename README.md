# ETL Project: Largest Banks by Market Capitalization

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) utilizando Python para procesar datos reales de los 10 bancos más grandes del mundo por capitalización de mercado.

El pipeline extrae datos de una tabla en Wikipedia, los transforma utilizando tasas de cambio, y los carga tanto en un archivo CSV como en una base de datos SQLite para su posterior análisis.

---

## Características principales

- **Extracción:** Utiliza web scraping para recuperar datos de una página web.
- **Transformación:** Convierte los valores de capitalización de mercado en dólares estadounidenses a GBP, EUR e INR usando un archivo de tasas de cambio.
- **Carga:** Almacena los datos procesados en:
  - Un archivo CSV local.
  - Una base de datos SQLite.
- **Consultas:** Permite realizar consultas SQL sobre la base de datos, como:
  - Listar todos los registros.
  - Calcular la capitalización de mercado promedio en GBP.
  - Recuperar los nombres de los 5 bancos más grandes.

---

## Tecnologías utilizadas

- **Lenguaje:** Python
- **Librerías:**
  - `pandas`: Para manipulación de datos.
  - `numpy`: Para operaciones matemáticas.
  - `requests`: Para realizar solicitudes HTTP.
  - `beautifulsoup4`: Para realizar web scraping.
  - `sqlite3`: Para la conexión y manejo de bases de datos.

---

## Estructura del repositorio

```
banks_project/
├── README.md               # Descripción del proyecto
├── banks_project.py        # Script principal del proyecto
├── exchange_rate.csv       # Archivo de tasas de cambio
├── output/                 # Carpeta para el archivo CSV generado
│   ├── Largest_banks_data.csv
├── database/               # Carpeta para la base de datos generada
│   ├── Banks.db
├── logs/                   # Carpeta para los registros de ejecución
│   ├── code_log.txt
```

---

## Cómo usar este proyecto

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:
```bash
git clone https://github.com/tuusuario/banks_project.git
```

### 2. Instalar dependencias

Asegúrate de tener Python instalado. Luego, instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```

### 3. Ejecutar el script

Ejecuta el script principal:
```bash
python banks_project.py
```

### 4. Resultados esperados

- **Archivo CSV:** Se genera en la carpeta `output/` con el nombre `Largest_banks_data.csv`.
- **Base de datos:** Se genera en la carpeta `database/` con el nombre `Banks.db`.
- **Registros:** Se guarda un archivo de logs en la carpeta `logs/` llamado `code_log.txt`.

---

## Queries disponibles

Ejecuta consultas en la base de datos SQLite para analizar los datos:

1. **Listar todos los registros:**
   ```sql
   SELECT * FROM Largest_banks;
   ```

2. **Calcular la capitalización promedio en GBP:**
   ```sql
   SELECT AVG(MC_GBP_Billion) FROM Largest_banks;
   ```

3. **Nombres de los 5 bancos más grandes:**
   ```sql
   SELECT `Bank name` FROM Largest_banks LIMIT 5;
   ```

---

## Propósito del proyecto

Este proyecto es una demostración práctica de habilidades en:
- Web scraping.
- Procesamiento y transformación de datos.
- Creación de pipelines ETL.
- Manejo de bases de datos SQLite.

Su principal proposito fue repasar conceptos y practicar.

---

## Autor

Creado por: **Enzo Ruiz Diaz**
- [LinkedIn](https://www.linkedin.com/in/enzo-ruiz-diaz/)
- [GitHub](https://github.com/tu-usuario/)

