# SECCION 002 D
# V 3
# fecha: 28/05
# hagan los ejercicios

"""
    ✔ 4. agregar menu para seleccionar:
        ✔ 1. Mostrar la lista numerada de animales (para poder seleccionar) 
        ✔ 1.5. solucionar posibles errores en seleccion
        ✔ 2. Poder 'filtrar' la lista de animales, segun el tipo
        3. Agregar animales a la lista (deben tener los mismos datos,
        nombre, tipo, peso, color)
"""

lista_animales = [
    {
        'nombre': 'pepito',
        'tipo' : 'gato',
        'peso' : 7.2, 
        'color' : 'naranjo',
    },
    {
        'nombre': 'jaimico',
        'tipo' : 'mandril',
        'peso' : 20.2, 
        'color' : 'plomo',
    },
    {
        'nombre': 'soy la comadreja',
        'tipo' : 'comadreja',
        'peso' : 7.2, 
        'color' : 'rojo',
    },
    {
        'nombre': 'mojojojo',
        'tipo' : 'mono',
        'peso' : 25.3, 
        'color' : 'verde',
    },
    {
        'nombre': 'mordecai',
        'tipo' : 'azulejo',
        'peso' : 2.2, 
        'color' : 'azul',
    },
    {
        'nombre': 'skips',
        'tipo' : 'yeti',
        'peso' : 200, 
        'color' : 'blanco',
    },
    {
        'nombre': 'rigby',
        'tipo' : 'mapache',
        'peso' : 8, 
        'color' : 'cafe',
    },
    {
        'nombre': 'pedro',
        'tipo' : 'mapache',
        'peso' : 5, 
        'color' : 'negro',
    },
    {
        'nombre': 'panxito',
        'tipo' : 'conejo',
        'peso' : 3, 
        'color' : 'verde',
    },
    {
        'nombre': 'panxote',
        'tipo' : 'conejo',
        'peso' : 10, 
        'color' : 'azul',
    },
]

menu = ["Mostrar lista enumerada de animales y seleeccionar uno", "Obtener un animal según su tipo", "Agregar un animal a la lista", "Salir"]
for numero, accion in enumerate(menu):
        print(f"{numero + 1} --> {accion}")

contador = 0

while True:
    eleccion = input("Qué acción desea realizar?: ")
    if eleccion == "1":
        for i, llave in enumerate(lista_animales): #recorre la lista y asigna un número a cada llave
            print(f"{i + 1} ---> {llave["nombre"]}, {llave["tipo"]}")
        seleccion = int(input("Seleccione el animal: ")) #ingresa id de animal
        if seleccion in range (1,11): #condicion de rango de lista
            animal_seleccionado = lista_animales[seleccion - 1] #recordar que la lista cuenta desde 0, por ende se debe restar 1 para obtener el id correcto 
            for key in animal_seleccionado.keys(): #recorre el diccionario
                print(f"{key} ---> {animal_seleccionado[key]}")
            continue
        else:
            print("Elemento inválido") #condicion de que la persona agregue un número mayor a los elementos o algún caracter inválido
            continue
    elif eleccion == "2":
        filtro  = input("Que tipo de animal desea obtener?: ").lower() #filtro
        for i in lista_animales: #recorro la lista de diccionarios
            if filtro in i.values(): #busco el nombre del filtro en los valores de cada diccionario
                contador += 1 #agregue un contador porque si xD
                print(f"El animal {i["nombre"]} es un {i["tipo"]}")
        print(f"hay {contador} animales de ese tipo")
        contador = 0
        continue
    elif eleccion == "3":
        print("Ingrese su nuevo animal") #nuevo animal
        nombre = input("Ingrese el nombre del animal: ").lower()
        tipo = input("Ingrese el tipo de animal: ")
        peso = int(input("Ingrese el peso del animal en Kg: "))
        color = input("Ingrese el color del animal: ")
        lista_animales.append({"nombre":nombre,"tipo":tipo,"peso":peso,"color":color}) #se agrega a la lista un diccionario con los datos proporcionados
        print(f"El animal de nombre {nombre} ha sido agregado correctamente a su lista") #indica que el animal ha sido ingresado correctamente
        print(lista_animales[-1]) #llamo al último elemento de la lista de diccionarios, osea el animal que agregamos
        print(input( )) #input de pausa, al presionar enter sigue corriendo el programa
        continue
    elif eleccion == "4": #condicion de salida
        print("Hasta pronto!")
        break
    else:
        print("Ingrese una acción válida") #condicion de que el usuario ingrese un número fuera del menú o un caracter inválido
        continue