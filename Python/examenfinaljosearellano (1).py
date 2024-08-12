import csv
import random
import math

# lista con nombre de personas/empleados
empleados = ['Enzo Castro', 'Manuel Correa', 'Ricardo Rios', 'Willy Urrutia', 'Maricel Gonzalez', 'Yerko Rojas', 'Maria Arellano']

# diccionario de trabajadores, para recorrer 
dicc_trabajadores = {empleado: 0 for empleado in empleados}

# asignacion de sueldos
def asignacion_sueldos():
    for empleado in dicc_trabajadores:
        sueldo = random.randint(300000, 2500000)
        dicc_trabajadores[empleado] = sueldo
    print('¡sueldos asignados con éxito!')

# clasificar los sueldos
def clasificar_sueldos():
    lista_menor = []
    lista_media = []
    lista_mayor = []
    total_sueldos = sum(dicc_trabajadores[x] for x in dicc_trabajadores)
    for trabajador in dicc_trabajadores:
        if dicc_trabajadores[trabajador] > 300000:
            lista_menor.append(trabajador)
        elif dicc_trabajadores[trabajador] >= 300000 and 2500000:
            lista_media.append(trabajador)
        elif dicc_trabajadores[trabajador] <= 2500000:
            lista_mayor.append(trabajador)
    print('Sueldos clasificados')
    total = len(lista_menor)
    print (f'sueldos menores a $300.000   total: {total}')
    for x in lista_menor:
        print (f'{x} -${dicc_trabajadores[x]}')
    total =len(lista_media)
    print(f'sueldos entre $300.000 y $2.500.000   total: {total}')
    for x in lista_media:
        total = len(lista_media)
        print (f'{x} -${dicc_trabajadores[x]}')
    total = len(lista_mayor)
    print(f'sueldos mayores a $2.500.000   total:{total}')
    for x in lista_mayor:
        total = len(lista_mayor)
        print(f'{x} -${dicc_trabajadores[x]}')
    print(f'total suma de sueldos:  ${total_sueldos}')


# estadisticas
def ver_estadisticas():
    sueldo_menor = min(dicc_trabajadores, key=dicc_trabajadores.get)
    sueldo_mayor = max(dicc_trabajadores, key=dicc_trabajadores.get)
    promedio_sueldos = sum(dicc_trabajadores.values()) / len(dicc_trabajadores)
    promedio_sueldos = math.prod(dicc_trabajadores.values())

    print(f'mostrar estadisticas')
    print(f'sueldo bajo: {sueldo_menor} -${dicc_trabajadores[sueldo_menor]}')
    print(f'sueldo mayor: {sueldo_mayor} -${dicc_trabajadores[sueldo_mayor]}')
    print(f'promedio de los sueldos: ${promedio_sueldos:.2f}')


# reporte de todo
def generar_reporte():
    with open ('reporte_sueldos_josearellano.csv', 'w', newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(['nombre empleado', 'sueldo base', 'descuento final', 'descuento afp', 'sueldo líquido'])
        for trabajador, sueldo in dicc_trabajadores.items():
            dcto_salud = round(sueldo * 0.07, 2)
            dcto_afp = round(sueldo * 0.12, 2)
            sueldo_liquido = sueldo - dcto_salud - dcto_afp
            writer.writerow ([trabajador, sueldo, dcto_afp, dcto_salud, sueldo_liquido])
        print('¡reporte generado con éxito!')


# menu en consola
while True:
    print('Bienvenido al menú! seleccione una opción (número)')
    print('1- asignar sueldos a empleados 2- clasificar 3- ver detalles 4- reporte de sueldos 5- salir')

    try:
        opcion = int(input('ingrese un número: '))
    except ValueError:
        print('ingrese algún numero válido: ')
        continue

    if opcion == 1:
        asignacion_sueldos()
    elif opcion == 2:
        clasificar_sueldos()
    elif opcion == 3:
        ver_estadisticas()
    elif opcion == 4:
        generar_reporte()
    elif opcion == 5:
        print('Finalizando programa...\nDesarrollado por José Arellano\nEstudiante Analista Programador Duoc UC - San Joaquin \nRUT 19.695.733-2')
        break
    else:
        print('No válido, intena otra vez...') 