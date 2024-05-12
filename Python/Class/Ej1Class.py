import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self, otro_punto):
        return math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
punto_plano_1 = Punto (3,4)
punto_plano_2 = Punto (8,9)

print(punto_plano_1)
print(punto_plano_1.distancia(punto_plano_2))

#primero defino la clase punto y le doi sus atributos
#defino despues el metodo de distancia el cual se obtiene al sacar
#la raiz cuadrada de la esta entre los cuadrados de los puntos
#defino el str para poder llamar al objeto y que me entregue el punto y no
#su lugar en la memoria RAM
#luego defino los objetos punto 1 y punto 2
#finalmente obtengo lo que deseo de los objetos

