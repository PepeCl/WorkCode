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


    def __repr__(self):
        return (f"Empleado ({self.nombre},{self.apellido},{self.sueldo})")
    
    def __str__(self):
        return (f"{self.nombre_completo()} - {self.correo_institucional()}")
    
    def __add__(self, other):
        return self.sueldo + other.sueldo
    
    def __len__(self):
        return len(self.nombre_completo())
    
emp_1 = Empleado("Giuseppe","Saavedra",50000)
emp_2 = Empleado("Tatiana","Contreras", 60000)
emp_3 = Empleado("Nino","Canino",70000)

print(emp_1.correo_institucional())

