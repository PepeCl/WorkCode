from random import randint

def asignar_sueldos(dict_trab):
    for i in dict_trab:
        sueldo_aleatorio = randint(300000,3000000)
        dict_trab[i] = sueldo_aleatorio
    return dict_trab

def clasificar_sueldos(dict_trab):
    menores ={}
    entre = {}
    superior ={}
    total_sueldos = []
    total = 0
    for trab,sueldo in dict_trab.items():
        total_sueldos.append(sueldo)
        if (sueldo < 800000):
            menores[trab] = sueldo
        elif (sueldo > 800000) and (sueldo < 2000000):
            entre[trab] = sueldo
        elif (sueldo > 2000000):
            superior[trab] = sueldo
    for sueldos in total_sueldos:
        total += sueldos

    return menores,entre,superior,total

def ver_estadisticas(dict_trab):
    maximo = {}
    minimo = {}
    sumador= 0
    multiplicador = 1
    valor_max = max(dict_trab.values())
    valor_min = min(dict_trab.values())
    for trab,sueldo in dict_trab.items():
        sumador += sueldo
        multiplicador *= sueldo
        if valor_max == sueldo:
            maximo[trab] = sueldo
        if valor_min == sueldo:
            minimo[trab] = sueldo
    promedio = (sumador / (len(dict_trab)))
    media_geometrica = int(multiplicador ** (1/len(dict_trab)))

    return maximo,minimo,promedio,media_geometrica

def reporte_de_sueldos(dict_trab):
    lista_dict = []
    for trab,sueldo in dict_trab.items():
        lista_dict.append({"Nombre Trabajador":trab,"Sueldo Base":sueldo})

    for trabajador in lista_dict:
        i = trabajador["Sueldo Base"]
        descuento_salud = int(i * 0.07)
        descuento_afp = int(i * 0.12)
        sueldo_liquido = int((i - (descuento_afp+descuento_salud)))
        trabajador["Descuento Salud"] = int(descuento_salud)
        trabajador["Descuento AFP"] = int(descuento_afp)
        trabajador["Sueldo Liquido"] = int(sueldo_liquido)

    return lista_dict




