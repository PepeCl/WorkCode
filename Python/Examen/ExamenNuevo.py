from random import randint
import csv

menu = ["Asignar Sueldos Aleatorios",
        "Clasificar Sueldos",
        "Ver Estadísticas",
        "Reporte de Sueldos",
        "Salir del Programa"]

trabajadores = {"Juan Perez":0,"María García":0,"Carlos López":0,"Ana Martinez":0,"Pedro Rodríguez":0,"Laura Hernández":0,"Miguel Sánchez":0,"Isabel Gómez":0,"Francisco Díaz":0,"Elena Fernández":0}

def asignar_sueldos():
    for worker in trabajadores:
        sueldo = randint(300000,3000000)
        trabajadores[worker] = sueldo
        print(f'{worker}--->${sueldo}')

def clasificar_sueldos():
    menores = {}
    entre = {}
    superiores = {}
    total = 0
    for trab,sueldo in trabajadores.items():
        total += sueldo
        if sueldo < 500000:
            menores[trab] = sueldo
        elif (sueldo >= 500000) and (sueldo < 2000000):
            entre[trab] = sueldo
        elif (sueldo > 2000000):
            superiores[trab] = sueldo
    print(f'\nSueldos menores a $500.000 TOTAL: {len(menores)}\n')
    print(f'Nombre Empleado ---> Sueldo')
    for a,b in menores.items():
        print(f'{a}---->${b}')

    print(f'\nSueldos entre $500.000 y $2.000.000 TOTAL: {len(entre)}\n')
    print(f'Nombre Empleado ---> Sueldo\n')
    for c,d in entre.items():
        print(f'{c}---->${d}')

    print(f'\nSueldos superiores a $2.000.000 TOTAL: {len(superiores)}\n')
    print(f'Nombre Empleado ---> Sueldo\n')
    for x,y in superiores.items():
        print(f'{x}---->${y}')
    
    print(f'\nTOTAL SUELDOS = ${total}\n')

def ver_estadisticas():
    minimo = {}
    maximo = {}
    multiplicador = 1
    sumador = 0
    valor_maximo = max(trabajadores.values())
    valor_minimo = min(trabajadores.values())
    for worker,sueldo in trabajadores.items():
        sumador += sueldo
        multiplicador *= sueldo
        if valor_maximo == sueldo:
            maximo[worker] = sueldo
        if valor_minimo == sueldo:
            minimo[worker] = sueldo
    promedio = (sumador / len(trabajadores))
    media = multiplicador ** (1/len(trabajadores))

    print(f'El sueldo más alto corresponde a: {maximo}\nEl sueldo más bajo corresponde a: {minimo}\nEl promedio de los sueldos es: ${promedio}\nLa media geométrica de sueldos es: ${media}')

def reporte_de_sueldos():
    lista_trabajadores = []
    for workers,payment in trabajadores.items():
        descuento_salud = round((payment * 0.07),1)
        descuento_afp = round((payment * 0.12),1)
        sueldo_liquido = round((payment - (descuento_afp + descuento_salud)),1)
        lista_trabajadores.append({"Nombre Trabajador":workers,"Sueldo Base":payment,"Descuento Salud":descuento_salud,"Descuento AFP":descuento_afp,"Sueldo Liquido":sueldo_liquido})

    with open("Reporte_GS_EX.csv","w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre Trabajador","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"])
        for trabajador in lista_trabajadores:
            print(trabajador)
            writer.writerow([trabajador["Nombre Trabajador"],trabajador["Sueldo Base"],trabajador["Descuento Salud"],trabajador["Descuento AFP"],trabajador["Sueldo Liquido"]])


while True:
    for i,j in enumerate(menu):
        print(f'{i+1} ---> {j}')

    accion = input("Ingrese la acción a realizar: ")

    if accion == "1":
        asignar_sueldos()

    if accion == "2":
        clasificar_sueldos()

    if accion == "3":
        ver_estadisticas()

    if accion == "4":
        reporte_de_sueldos()

    if accion == "5":
        break

        
    



