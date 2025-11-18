import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfVideoJuegos = pd.read_csv("RA3/VideoGamesSales.csv",sep=";")
print(dfVideoJuegos.head())
print("--------------------------------------------------------")
print(dfVideoJuegos.info)
print("--------------------------------------------------------")
print(dfVideoJuegos.describe)
dfVideoJuegos["release_date"] = pd.to_datetime(dfVideoJuegos["release_date"])
