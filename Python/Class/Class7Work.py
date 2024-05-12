class Empleado:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    @property    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    @property
    def correo(self):
        return f"{self.nombre}.{self.apellido}@boltzspa.com"
    
    @nombre_completo.setter
    def nombre_completo(self, name):
        nombre, apellido = name.split(" ")
        self.nombre = nombre
        self.apellido = apellido

    @nombre_completo.deleter
    def nombre_completo(self):
        print("Borrar nombre")
        self.nombre = None
        self.apellido = None
    
emp_1 = Empleado("Nino","Canino")

emp_1.nombre_completo = "Nano Canano"

print(emp_1.nombre)
print(emp_1.apellido)
print(emp_1.nombre_completo)
print(emp_1.correo)
print(emp_1.__dict__)

del emp_1.nombre_completo
print(emp_1.nombre)