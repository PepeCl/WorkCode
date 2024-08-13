import matplotlib.pyplot as plt
import numpy as np

"""La variable independiente es el tiempo [hr] y la variable dependiente es la temperatura[°C]"""

"""El dominio para este caso son todos los reales comprendidos entre el 0 y el 9 (ya que son 9 horas de trabajo)"""

def funcion_temperatura(tiempo):
    temperatura = (-0.5)*(tiempo ** 2) + 3 * tiempo + 20
    return temperatura

tiempo = np.arange(0,9,1)
temperatura = funcion_temperatura(tiempo)
plt.plot(tiempo,temperatura)
plt.xlabel("Horas Trabajadas")
plt.ylabel("Temperatura servidor")
plt.grid(True)
plt.show()

"""Mediante análisis gráfico se puede ver que la máxima temperatura se alcanza a las 3 horas de trabajo, es decir a las 11 am"""
#si nos basamos en el concepto de calculo de máximos y mínimos mediante la derivada de las funciones entonces tenemos que:
#f'(x) = -t + 3
#Para máximo/minimo la derivada debe ser 0, por ende
#0 = -t + 3
#t = 3
#coincide con el análisis gráfico

print(f"La temperatura del servidor a las 13:00 (5 horas de trabajo) es {funcion_temperatura(5)} °C")
print(f"La temperatura del servidor a las 18:00 (9 horas de trabajo) es {funcion_temperatura(9)} °C")
