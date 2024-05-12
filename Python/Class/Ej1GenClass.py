class Empleados:
    cant_empleados = 0
    def __init__(self, nombre, cargo, sueldo, año_ingreso):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo
        self.año_ingreso = año_ingreso

class Compañia:
    def __init__(self, nombre):
        self.nombre=nombre
        self.empleados = []

    def salario_total_empresa(self):
        return sum(emp.sueldo for emp in self.empleados)
    
    def agregar_empleado(self, empleado):
        if empleado not in self.empleados:
            self.empleados.append(empleado)

    def obtener_lista_empleados(self):
        return [emp.nombre for emp in self.empleados]
    
comp = Compañia("Nino Enterprises")

emp_1 = Empleados ("Giuseppe Saavedra", "Programador",50000,2024)
emp_2 = Empleados ("Tatiana Contreras", "Ejecutiva Comercial",60000,2023)
emp_3 = Empleados ("Nino Canino", "Perro", 0, 2021)

comp.agregar_empleado(emp_1)
comp.agregar_empleado(emp_2)
comp.agregar_empleado(emp_3)

print(comp.obtener_lista_empleados())
print(comp.salario_total_empresa())

print(comp.empleados)
        