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
        4. Eliminar Animal
            - mostrar la lista
            - seleccionar que cosa eliminar

        5.- Modificar el dato de un animal

        6.- Agregar un dato (llave : valor) a un animal         
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


def lista_enumerada(lista): #se define la función, la cual acepta una lista como variable de entrada
    for numero , llave in enumerate(lista): 
        print(f"{numero + 1} ---> {llave["nombre"]},{llave["tipo"]}")
    
def seleccionar_animal(id,lista): #se define la funcion de seleccionar animal la cual acepta la id o el numero que ingresa el usuario y la lista de animales
    if id in range (len(lista)): #condicion de rango de lista
        animal_selec = lista[id - 1] 
        for key in animal_selec.keys():
            print(f"{key} ---> {animal_selec[key]}")
    else:
        print("Elemento inválido")

def filtro(tipo,lista): #funcion de filtro que acepta como variables de entrada el tipo de animal y la lista de animales
    for i in lista:
        if tipo in i.values():
            print(f"El animal {i["nombre"]} es un {i["tipo"]}")
        
def agregar_animal(nombre,type,weight,color,lista): #función de agregar animales a la lista, acepta como variables de entrada el nombre, tipo, peso, color y la lista de animales
    lista.append({"nombre":nombre,"tipo":type,"peso":weight,"color":color})
    print(f"El animal {nombre} ha sido agregado correctamente")

def eliminar_animal(nombre,lista):
    contador = True #condicion de rango de lista
    for animal in lista:
        if nombre in animal.values():
            lista.remove(animal)
            contador = False
            print(f"el animal {nombre} ha sido eliminado correctamente")
    if contador == True:
        print ("El animal no está en la lista, ingrese un nombre válido")


def modificar_atributo(id,llave,valor_modificado,lista):
    if llave in (lista[id - 1].keys()):
        (lista[id - 1]).update({llave:valor_modificado})
        print(f"El animal {id} ha sido modificado correctamente")
    else:
        (lista[id - 1]).update({llave:valor_modificado})
        print(f"La característica del animal {id} ha sido agregado correctamente")

menu = ["Mostrar lista enumerada de animales y seleeccionar uno", "Obtener un animal según su tipo", "Agregar un animal a la lista",
        "Eliminar animal de la lista", "Modificar animal", "Salir"]
for numero, accion in enumerate(menu):
        print(f"{numero + 1} --> {accion}")

while True:
    eleccion = input("Qué acción desea realizar?: ")
    if eleccion == "1":
        lista_enumerada(lista_animales)
        animal = int(input("Ingrese el ID del animal: "))
        seleccionar_animal(animal,lista_animales)
        continue
    elif eleccion == "2":
        tipo = input("Ingrese el tipo de animal: ")
        filtro(tipo,lista_animales)
        continue
    elif eleccion == "3":
        print("Ingrese su nuevo animal") #nuevo animal
        nombre = input("Ingrese el nombre del animal: ").lower()
        tipo = input("Ingrese el tipo de animal: ")
        peso = int(input("Ingrese el peso del animal en Kg: "))
        color = input("Ingrese el color del animal: ")
        agregar_animal(nombre,tipo,peso,color,lista_animales)
        print(lista_animales[-1])
        continue
    elif eleccion == "4": #condicion de eliminar animal
        eliminar  = input ("Dame el nombre del animal que deseas eliminar: ")
        eliminar_animal(eliminar,lista_animales)
        continue
    elif eleccion == "5": #condicion de salida
        id = int(input("Ingrese el ID del animal a modificar: "))
        if id not in range (len(lista_animales)+1):
            print("ID fuera de rango, ingrese un número válido")
        else:
            llave = input("Ingrese el atributo a modificar (Nombre/Tipo/Peso/Color): ").lower()
            if llave not in lista_animales[id-1].keys():
                print("*****Esa característica no existe, se agregará como nueva*****") 
            modificacion = input("Ingrese el nuevo valor: ")
            modificar_atributo(id,llave,modificacion,lista_animales)
            print(lista_animales[id-1])
        continue
    elif eleccion == "6": #condicion de salida
        print("Hasta pronto!")
        break
    else:
        print("Ingrese una acción válida") #condicion de que el usuario ingrese un número fuera del menú o un caracter inválido
        continue

        

