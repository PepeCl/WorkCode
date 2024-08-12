menu = ["Asignar Sueldos Aleatorios",
        "Clasificar Sueldos",
        "Ver Estadísticas",
        "Reporte de Sueldos",
        "Salir del Programa"]

trabajadores = {"Juan Perez":0,"María García":0,"Carlos López":0,"Ana Martinez":0,"Pedro Rodríguez":0,"Laura Hernández":0,"Miguel Sánchez":0,"Isabel Gómez":0,"Francisco Díaz":0,"Elena Fernández":0}


from funcex import *
import csv

while True:
    for id,opcion in enumerate(menu):
        print (f"{id+1} ---> {opcion}")
    
    accion = input("Ingrese la acción a realizar: ")

    if accion == "1":
        list_trab = asignar_sueldos(trabajadores)
        for trab,sueldo in trabajadores.items():
            print(f"{trab} -> ${sueldo}")

    if accion == "2":
        menores,entre,superiores,total = clasificar_sueldos(list_trab)
        print(f"\nSueldos menores a $800.000 TOTAL: {len(menores)}\n")
        print("Nombre Empleado      Sueldo")
        for trab,sueldo in menores.items():
            print(f"{trab}      ${sueldo}")
        
        print(f"\nSueldos entre $800.000 y $2.000.000 TOTAL: {len(entre)}\n")
        print("Nombre Empleado      Sueldo")
        for trab,sueldo in entre.items():
            print(f"{trab}      ${sueldo}")

        print(f"\nSueldos superiores a $2.000.000 TOTAL: {len(superiores)}\n")
        print("Nombre Empleado      Sueldo")
        for trab,sueldo in superiores.items():
            print(f"{trab}      ${sueldo}")
        
        print(f"\nTOTAL SUELDOS: ${total}")
    
    if accion == "3":
        max,min,promedio,media = ver_estadisticas(list_trab)
        print(f"El sueldo mínimo corresponde a: {min}\nEl sueldo máximo corresponde a: {max}\nEl promedio de sueldos es: ${promedio}\nLa media geométrica es: ${media}")
    
    if accion == "4":
        lista_trabajadores = reporte_de_sueldos(list_trab)

        with open ("Reporte_Sueldos_Giuseppe_Saavedra.csv","w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre Trabajador","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"])
        
            for trabajador in lista_trabajadores:
                print(trabajador)
                writer.writerow([trabajador["Nombre Trabajador"],trabajador["Sueldo Base"],trabajador["Descuento Salud"],trabajador["Descuento AFP"],trabajador["Sueldo Liquido"]])

    
    if accion == "5":
        print("Finalizando Programa...\nDesarrollado por: Giuseppe Saavedra\nRut:18.094.814-7")
        break
    
    