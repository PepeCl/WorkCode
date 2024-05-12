#qué pasa si por ejemplo nuestros empleados están en una base de datos y sus
#datos se nos entregan de la siguiente manera : nombre-apellido-edad-sueldo

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
    def from_string(cls, emp_str):
        nombre, apellido, edad, pago = emp_str.split("-")
        return cls(nombre, apellido, edad, pago)
        
    @staticmethod 
    def es_findesemana(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return "Es Fin de Semana"
        else:
            return "Es día laboral"
    #en python los días están programados para ser contados desde el
    #0 = lunes hasta el 6 = domingo
    
emp_1 = "Giuseppe-Saavedra-32-60000"
emp_2 = "Tatiana-Contreras-31-70000"
emp_3 = "Nino-Canino-2-80000"

new_emp_1=Empleado.from_string(emp_1) #se asigna la información a un nuevo diccionario

#print(new_emp_1.nombre)
#print(new_emp_1.__dict__) #se puede ver claramente el nuevo diccionario creado

import datetime
mi_dia = datetime.date(2024, 4, 28)
print(Empleado.es_findesemana(mi_dia))