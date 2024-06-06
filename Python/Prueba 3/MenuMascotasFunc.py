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
    if id in range (len(lista)+1): #condicion de rango de lista
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
    contador = True #verifica si el animal está o no en la lista
    for animal in lista: #recorro la lista 
        if nombre in animal.values(): #si el nombre se encuentra en los valores entonces que haga lo que sige más adelante
            lista.remove(animal)
            contador = False #cambia la condicion para guardar que el animal sí existe en el diccionario
            print(f"el animal {nombre} ha sido eliminado correctamente")
    if contador == True: #en caso que el animal no esté en la lista sigue este proceso
        print ("El animal no está en la lista, ingrese un nombre válido")


def modificar_atributo(id,llave,valor_modificado,lista): #funcion de atributo, acepta id, valor a modificar,valor modificado y la lista
    if llave in (lista[id - 1].keys()): #llama al diccionario que se encuetra en la posición i - 1 ingresada por el usuario. Si el valor está en la lista entonces hace lo siguiente
        (lista[id - 1]).update({llave:valor_modificado}) #actualiza el valor
        print(f"El animal {id} ha sido modificado correctamente") #imprime que el animal fue modificado
    else: #en caso que el valor no se encuentre en la lista de características del animal, entonces hace lo siguiente
        (lista[id - 1]).update({llave:valor_modificado}) #actualiza el valor segun el comando update, el cual agrega la nueva característica al final del diccionario
        print(f"La característica del animal {id} ha sido agregado correctamente") #imprime que la característica se agregó

menu = ["Mostrar lista enumerada de animales y seleeccionar uno", "Obtener un animal según su tipo", "Agregar un animal a la lista",
        "Eliminar animal de la lista", "Modificar animal", "Salir"]
for numero, accion in enumerate(menu):
        print(f"{numero + 1} --> {accion}")

while True:
    eleccion = input("Qué acción desea realizar?: ")
    if eleccion == "1": #accion de menu 1
        lista_enumerada(lista_animales) #llama a la funcion lista enumerada
        animal = int(input("Ingrese el ID del animal: ")) #pregunta por la id
        seleccionar_animal(animal,lista_animales) #llama a la funcion de seleccionar animal por ID
        continue
    elif eleccion == "2": #acción menú 2
        tipo = input("Ingrese el tipo de animal: ") #pregunta por el tipo de animal
        filtro(tipo,lista_animales) #llama a la función filtro
        continue
    elif eleccion == "3": #acción menú 3
        print("Ingrese su nuevo animal") #nuevo animal
        nombre = input("Ingrese el nombre del animal: ").lower() #características del nuevo animal
        tipo = input("Ingrese el tipo de animal: ")
        peso = int(input("Ingrese el peso del animal en Kg: "))
        color = input("Ingrese el color del animal: ")
        agregar_animal(nombre,tipo,peso,color,lista_animales) #llama a la función de agregar animal
        print(lista_animales[-1]) #imprime el último animal agregado, ya que se hace con la función append (agrega el elemento al final de la lista)
        continue
    elif eleccion == "4": #condicion de eliminar animal
        eliminar  = input ("Dame el nombre del animal que deseas eliminar: ") #llama al animal a eliminar por el nombre, se puede cambiar a ID
        eliminar_animal(eliminar,lista_animales) #llama a la funcion eliminar animal
        continue
    elif eleccion == "5": #acción menú 5
        id = int(input("Ingrese el ID del animal a modificar: ")) #ingresa el ID del animal a modificar
        if id not in range (len(lista_animales)+1): #se usa id not in range (len(lista)+1) ya que el range va desde el 0 hasta el elemento final -1. ej: range (10) --> 0123456789
            print("ID fuera de rango, ingrese un número válido") #si el ID no está en el rango del largo de la lista entonces imprime fuera de rango ()
        else:
            llave = input("Ingrese el atributo a modificar (Nombre/Tipo/Peso/Color): ").lower() #pregunta por el atributo/característica a modificar
            if llave not in lista_animales[id-1].keys(): #como cada elemento de la lista es un diccionario, entonces lo podemos tratar con el comando keys()
                print("*****Esa característica no existe, se agregará como nueva*****") #imprime este mensaje en caso que la característica no esté en el diccionario
            modificacion = input("Ingrese el nuevo valor: ") #nuevo valor
            modificar_atributo(id,llave,modificacion,lista_animales) #llama a la función modificar_atributo
            print(lista_animales[id-1]) #imprime el animal seleccionado. recordar que ponemos id - 1 ya que el programa cuenta desde el 0, por ende elemento 10 del usuario es el elemento 9 de la lista
        continue
    elif eleccion == "6": #condicion de salida
        print("Hasta pronto!")
        break
    else:
        print("Ingrese una acción válida") #condicion de que el usuario ingrese un número fuera del menú o un caracter inválido
        continue

        

