
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("images/production_by_day.png", dpi=300, bbox_inches="tight")
plt.show()



plt.bar(
    df["Day"],
    df["Defects"],
    color=["darkcyan","darkcyan","darkcyan","darkcyan","darkgreen","crimson","darkcyan"]
    ) # Esto crea un gráfico de barras utilizando la columna "Day" para el eje x y la columna "Defects" para el eje y.
plt.title("Defects by Day")
plt.xlabel("Day")
plt.ylabel("Defects")
plt.ylim(0,100)
for day, defects in zip(df["Day"], df["Defects"]): 
    plt.text(day, defects +1, str(defects),ha="center") # Esto agrega etiquetas de texto encima de cada barra en el gráfico, mostrando el valor de defectos correspondiente a cada día. El texto se coloca un poco por encima de la barra (defects + 15) para que sea visible.
plt.show()

plt.scatter(df["Downtime_Minutes"], df["Defects"], color="darkcyan", s=100, alpha=0.8,) # Esto crea un gráfico de dispersión utilizando la columna "Downtime_minutes" para el eje x y la columna "Defects" para el eje y. Cada punto en el gráfico representa un día específico, con su tiempo de inactividad en minutos y el número de defectos correspondientes.
plt.grid(alpha=0.3)
plt.xlim(5,75)
plt.ylim(15,65)
plt.title("Defects vs Downtime")
plt.xlabel("Downtime (minutes)")
plt.ylabel("Defects")
plt.show()



pendiente, intercepto = np.polyfit(
    df["Downtime_Minutes"],
    df["Defects"],
    1
)

y_linea = pendiente * df["Downtime_Minutes"] + intercepto

plt.scatter(df["Downtime_Minutes"], df["Defects"], color="darkcyan", s=100, alpha=0.8,label="Actual data") # Esto crea un gráfico de dispersión utilizando la columna "Downtime_minutes" para el eje x y la columna "Defects" para el eje y. Cada punto en el gráfico representa un día específico, con su tiempo de inactividad en minutos y el número de defectos correspondientes.

plt.plot(
    df["Downtime_Minutes"],
    y_linea,
    color="crimson",
    linewidth=3,
    label="Trend Line"
    
)
plt.legend()
plt.tight_layout()
plt.savefig("images/defects_vs_downtime.png", dpi=300, bbox_inches="tight")
plt.show()
# Esto realiza un ajuste de línea recta (grado 1) a los datos de "Downtime_minutes" y "Defects". Devuelve los coeficientes de la línea ajustada, donde el primer valor es la pendiente y el segundo valor es la intersección con el eje y. Estos coeficientes se pueden usar para trazar la línea de tendencia en el gráfico de dispersión.
