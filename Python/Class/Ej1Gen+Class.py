class Compañia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        if empleado not in self.empleados:
            self.empleados.append(empleado)
    
    def sueldos_totales(self):
        return sum(emp.sueldo for emp in self.sueldo)

    
    
class Empleados(Compañia):
    def __init__(self, nombre, nombre_emp, cargo, sueldo, año):
        super().__init__(nombre)
        self.nombre_emp = nombre_emp
        self.cargo = cargo
        self.sueldo = sueldo
        self.año =año

    
comp = Compañia("Nino Enterprises")

emp_1 = Empleados ("Nino Enterprises" ,"Giuseppe Saavedra", "Programador",50000,2024)
emp_2 = Empleados ("Nino Enterprises","Tatiana Contreras", "Ejecutiva Comercial",60000,2023)
emp_3 = Empleados ("Nino Enterprises","Nino Canino", "Perro", 0, 2021)

comp.agregar_empleado(emp_1)
comp.agregar_empleado(emp_2)
comp.agregar_empleado(emp_3)

print(comp.sueldos_totales())

#el programa genera error ya que primero debo definir la clase de empleados que 
#reciba el método de sueldo, y no al revés aunque desee aplicar que la clase
#empleado sea una subclase de la clase compañia.
