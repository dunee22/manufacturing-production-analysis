
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/production_data.csv") # Asegúrate de que la ruta al archivo CSV sea correcta. Si el archivo está en el mismo directorio que tu script, puedes usar simplemente "production_data.csv". Si está en una carpeta llamada "data", entonces la ruta es "data/production_data.csv".
print(df)

# print(df.info()) Esto nos da información sobre el DataFrame, como el número de filas, columnas, tipos de datos y valores nulos.

# print(df.describe()) Esto nos proporciona estadísticas descriptivas sobre las columnas numéricas del DataFrame, como la media, la desviación estándar, los valores mínimos y máximos, y los percentiles.

max_defects = df["Defects"].max() # Esto encuentra el valor máximo en la columna "Defects", que representa el número máximo de defectos registrados en un día.
print(f"Maximum defects: {max_defects}")

most_defects_day = df[df["Defects"] == max_defects] # Esto filtra el DataFrame para obtener solo las filas donde el número de defectos es igual al valor máximo encontrado. Esto nos dará un nuevo DataFrame que contiene solo los días con el número máximo de defectos.

print(f"Day with most defects: {most_defects_day['Day'].iloc[0]}") # Esto accede a la columna "Day" del DataFrame filtrado (most_defects_day) y obtiene el primer valor de esa columna usando iloc[0]. Esto nos dará el día específico en el que se registró el número máximo de defectos.

average_defects = df["Defects"].mean()

above_average_defects =df[df["Defects"] > average_defects] # Esto filtra el DataFrame para obtener solo las filas donde el número de defectos es mayor que el promedio calculado. Esto nos dará un nuevo DataFrame que contiene solo los días con un número de defectos por encima del promedio.

print(f"Average defects: {average_defects:.2f}")
print("Days with above average defects:")
print(above_average_defects[["Day", "Defects"]]) # Esto imprime solo las columnas "Day" y "Defects" del DataFrame filtrado (above_average_defects), mostrando los días específicos y el número de defectos para aquellos días que tienen un número de defectos por encima del promedio.

max_production = df["Production"].max()
print(f"Maximum production: {max_production}")

max_production_day = df[df["Production"] == max_production]
print(f"Day with maximum production: {max_production_day['Day'].iloc[0]}") # Esto accede a la columna "Day" del DataFrame filtrado (max_production_day) y obtiene el primer valor de esa columna usando iloc[0]. Esto nos dará el día específico en el que se registró la producción máxima.
print(f"Production: {max_production_day['Production'].iloc[0]}") # Esto imprime solo las columnas "Day" y "Production" del DataFrame filtrado (max_production_day), mostrando el día específico y el número de unidades producidas para el día con la producción máxima.

plt.bar(
    df["Day"],
    df["Production"],
    color=["darkcyan","darkcyan","darkcyan","darkcyan","darkgreen","crimson","darkcyan"]
    ) # Esto crea un gráfico de barras utilizando la columna "Day" para el eje x y la columna "Production" para el eje y.
plt.title("Production by Day")
plt.xlabel("Day")
plt.ylabel("Production")
plt.ylim(0,1600)
for day, production in zip(df["Day"], df["Production"]): 
    plt.text(day, production + 15, str(production),ha="center") # Esto agrega etiquetas de texto encima de cada barra en el gráfico, mostrando el valor de producción correspondiente a cada día. El texto se coloca un poco por encima de la barra (production + 15) para que sea visible.
plt.show()