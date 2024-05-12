class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre 
        self.salario = salario
        self.departamento = departamento

    def __repr__(self):
        return (f"Empleado ({self.nombre}, {self.salario}, {self.departamento})")
    
emp_1 = Empleado("Nino Canino", 50000, "Departamento de Hambre Extrema")

print(emp_1)