class Rectangulo:
    def __init__(self, altura, ancho):
        self.altura = altura
        self.ancho = ancho
    
    def perimetro(self):
        return (2*self.altura + 2*self.ancho)
    
    def area (self):
        return (self.altura * self.ancho)
    
    def __str__(self):
        return f"Rectángulo de altura {self.altura} y de ancho {self.ancho}"
    
rect_1 = Rectangulo(4,5)
rect_2 = Rectangulo(10,30)

print(rect_1)
print(rect_2)
print(rect_1.area())
print(rect_2.perimetro())