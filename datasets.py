import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfVideoJuegos = pd.read_csv("RA3/VideoGamesSales.csv",sep=";")
print(dfVideoJuegos.head())
print("--------------------------------------------------------")
#print(dfVideoJuegos.info)
print("--------------------------------------------------------")
#print(dfVideoJuegos.describe)
dfVideoJuegos["release_date"] = pd.to_datetime(dfVideoJuegos["release_date"] ,dayfirst=True, errors="coerce")
dfVideoJuegos["last_update"] = pd.to_datetime(dfVideoJuegos["last_update"] ,dayfirst=True, errors="coerce")
print(dfVideoJuegos.head())
# Conteo de valores nulos por columna
print("Valores nulos por columna:")
print(dfVideoJuegos.isna().sum())
dfVideoJuegos.fillna({'critic_score': 0, 'total_sales': 0}, inplace=True)
#Corregir formato, coma en vez de punto
dfVideoJuegos['total_sales'] = (dfVideoJuegos['total_sales'].astype(str).str.replace(',', '.'))



