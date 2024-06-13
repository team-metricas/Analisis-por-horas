# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:01:46 2024

@author: 20171078343
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# Cambio al directorio de datos
os.chdir("../data/")

# Cargo los datos desde el archivo CSV
archivo_csv = "medidas_01.csv"
df = pd.read_csv(archivo_csv)

# Agrupo los datos por "hora" y veo estadísticas descriptivas para "impacto"
df_grouped = df.groupby('hora')['impacto'].describe()

# Redondeo las columnas 'mean' y 'std' a 2 decimales porque queda mal en excel
df_grouped['mean'] = df_grouped['mean'].round(2)
df_grouped['std'] = df_grouped['std'].round(2)

# Elimino las columnas 25 y 75 del DataFrame agrupado
df_grouped.drop(['25%', '75%'], axis=1, inplace=True)

# Renombro la columna '50%' como 'Mediana'
df_grouped.rename(columns={'50%': 'Mediana'}, inplace=True)

# veo en la IDE del Spyder
print(df_grouped)

# Guardo los descriptores estadísticos en un archivo CSV en la raiz del repo
descriptores_csv = "descriptores_estadisticos.csv"
df_grouped.to_csv('../'+descriptores_csv, sep=';', encoding='utf-8-sig')

# Grafico la distribución de "impacto" por "hora"
plt.figure(figsize=(10, 6))
plt.plot(df_grouped.index, df_grouped['mean'], marker='o', linestyle='-', color='b', label='Media')
plt.fill_between(df_grouped.index, df_grouped['mean'] - df_grouped['std'], df_grouped['mean'] + df_grouped['std'], color='b', alpha=0.2, label='Desviación Estándar')
plt.xlabel('Hora')
plt.ylabel('Impacto')
plt.title('Distribución de Impacto por Hora')
plt.legend()
plt.grid(True)

# Guardo el gráfico como archivo PNG en la raíz del repo
grafico_png = "grafico_impacto_por_hora.png"
plt.savefig('../'+grafico_png)

# Muestro el gráfico en la interfaz de Spyder
plt.show()
