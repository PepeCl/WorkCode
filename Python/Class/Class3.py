class Empleado:
    reajuste_sueldo = 1.05
    numero_empleados = 0

    def __init__(self, nombre, apellido, edad, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sueldo = sueldo

        Empleado.numero_empleados += 1

    def ipc_sueldo(self):
        if self.sueldo < 60000:
            self.sueldo = self.sueldo * self.reajuste_sueldo
        return self.sueldo

    def correo_institucional(self):
        return (f"{self.nombre}.{self.apellido}.{self.edad[0]}@boltzspa.com")
    
    def contrasena_correo(self):
        return(f"{self.nombre[0:2]}.{self.apellido[0:3]}_{self.edad[::-1]}")
    
    @classmethod
    def aplica_reajuste_sueldo(cls, monto): #classmethod, llamo a la clase y le doi un metodo nuevo
        cls.reajuste_sueldo = monto #acá hago que al ingresar cualquier monto, me cambie el valor de la variable inicial de reajuste
    
    
emp_1 = Empleado("Giuseppe","Saavedra", "32" , 50000)
emp_2 = Empleado("Tatiana","Contreras", "31" , 60000)
emp_3 = Empleado("Nino","Canino","3", 70000)

Empleado.aplica_reajuste_sueldo(1.07)
print(emp_1.reajuste_sueldo) #acá podemos ver que se cambia el valor de la variable de reajuste asignado en la clase

print(emp_1.sueldo)
print(emp_2.sueldo)
print(emp_3.sueldo)

emp_2.ipc_sueldo()

print(Empleado.numero_empleados)

#print(emp_1.correo_institucional())
#print(emp_2.correo_institucional())
#print(emp_3.correo_institucional())

#print(emp_1.contrasena_correo().lower())

#print(emp_1.__dict__) # la clase transforma los datos proporcionados en un diccionario asociando cada variable a su valor.
#print(Empleado.__dict__) #se pueden ver cosas interesantes al llamar al diccionario de la clase completa