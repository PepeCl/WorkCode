import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def determinar_largo(tiempo):
    largo = 1.85 * tiempo
    return largo

def buscar_cero(tiempo):
    return 1.85*tiempo - 6600
"""
tiempo_transcurrido = float(input("Ingrese el tiempo transcurrido en HORAS (hr): "))
print(f"Tras {tiempo_transcurrido} [hr] se han instalado {determinar_largo(tiempo_transcurrido)} [km] de cable")

"""

""" La variable independiente en este caso es el tiempo [hr] y la variable dependiente es el largo [km] """

""" El dominio de la función es todos los reales positivos y el cero """

"""
tiempo = np.arange(0,10,1)
largo = 1.85 * (tiempo)
plt.plot(tiempo,largo)
plt.xlabel("Tiempo Transcurrido [seg]")
plt.ylabel("Largo de cable instalado [Km]")
plt.grid(True)
plt.show()
"""

print(f"Tras 148 [hr] se han instalado {determinar_largo(148)} [km] de cable")
print(f"Tras 2300 [hr] se han instalado {determinar_largo(2300)} [km] de cable")

tiempo_trabajo = 3480 / 1.85

print(f"Tras 3480 [Km] de cable instalado se ha trabajado {tiempo_trabajo} [hr]")

tiempo_obra = 6600 / 1.85

print(f"Para completar la obra se necesitó de {tiempo_obra} [hr] de trabajo")

solucion = fsolve(buscar_cero,6600)

print(solucion)