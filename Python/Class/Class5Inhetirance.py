class Empleado:
    reajuste_sueldo = 1.05
    numero_empleados = 0

    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo

        Empleado.numero_empleados += 1

    def ipc_sueldo(self):
        self.sueldo = int(self.sueldo * self.reajuste_sueldo)

    def correo_institucional(self):
        return (f"{self.nombre}.{self.apellido}@boltzspa.com")
    
    def contrasena_correo(self):
        return(f"{self.nombre[0:2]}.{self.apellido[0:3]}_{self.edad[::-1]}")

    def nombre_completo(self):
        return (f"{self.nombre} {self.apellido}")

class Desarrolladores(Empleado):
    reajuste_sueldo = 1.1

    def __init__(self, nombre, apellido, sueldo, leng_progra):
        super().__init__(nombre,apellido,sueldo)
        self.leng_progra = leng_progra


class Manager(Empleado):

    def __init__(self, nombre, apellido, sueldo, empleados=None):
        super().__init__(nombre,apellido,sueldo)
        if empleados is None:
            self.empleados = []
        else:
            self.empleados = empleados
    
    def agregar_empleados(self, emp):
        if emp not in self.empleados:
            self.empleados.append(emp)

    def quitar_empleados(self, emp):
        if emp in self.empleados:
            self.empleados.remove(emp)

    def imprimir_empleados(self):
        for emp in self.empleados:
            print("-->", emp.nombre_completo())
        
   
dev_1 = Desarrolladores("Giuseppe","Saavedra",50000,"Python")
dev_2 = Desarrolladores("Tatiana","Contreras", 60000,"JavaScript")
dev_3 = Desarrolladores("Nino","Canino",70000, "C#")

mgr_1=Manager("Susana","Smith", 90000, [dev_1])

mgr_1.agregar_empleados(dev_2)

mgr_1.imprimir_empleados()

print(mgr_1.nombre)