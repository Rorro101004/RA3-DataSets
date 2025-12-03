import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar dataset
dfVideoJuegos = pd.read_csv("RA3/VideoGamesSales.csv", sep=";")
print("=== Primeras filas del dataset ===")
print(dfVideoJuegos.head(), "\n")

# 2. Convertir columnas de fechas
dfVideoJuegos["release_date"] = pd.to_datetime(dfVideoJuegos["release_date"], dayfirst=True, errors="coerce")
dfVideoJuegos["last_update"] = pd.to_datetime(dfVideoJuegos["last_update"], dayfirst=True, errors="coerce")

print("=== Dataset con fechas convertidas ===")
print(dfVideoJuegos.head(), "\n")

# 3. Conteo de valores nulos
print("=== Valores nulos por columna ===")
print(dfVideoJuegos.isna().sum(), "\n")

# 4. Rellenar nulos en critic_score y total_sales
dfVideoJuegos.fillna({'critic_score': 0, 'total_sales': 0}, inplace=True)

# 5. Corregir formato de total_sales (coma → punto → float)
dfVideoJuegos['total_sales'] = (
    dfVideoJuegos['total_sales'].astype(str).str.replace(',', '.').astype(float)
)

# 6. Crear columna de ventas regionales
dfVideoJuegos['regional_sales_sum'] = (
    dfVideoJuegos['na_sales'] +
    dfVideoJuegos['jp_sales'] +
    dfVideoJuegos['pal_sales'] +
    dfVideoJuegos['other_sales']
)

print("=== Comparación total_sales vs regional_sales_sum ===")
print(dfVideoJuegos[['title', 'total_sales', 'regional_sales_sum']].head(10), "\n")

# 7. Porcentaje de ventas en Norteamérica
dfVideoJuegos['sales_na_pct'] = dfVideoJuegos['na_sales'] / dfVideoJuegos['total_sales']

print("=== Ventas en Norteamérica (primeras filas) ===")
print(dfVideoJuegos[['title', 'na_sales', 'total_sales', 'sales_na_pct']].head(10), "\n")

# 8. Edad del juego desde lanzamiento hasta última actualización
dfVideoJuegos['age_days_since_release'] = (
    dfVideoJuegos['last_update'] - dfVideoJuegos['release_date']
).dt.days

print("=== Edad del juego en días (10 filas al azar) ===")
print(dfVideoJuegos[['title', 'release_date', 'last_update', 'age_days_since_release']].sample)
