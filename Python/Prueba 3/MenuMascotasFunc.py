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


def lista_enumerada(lista):
    for numero , llave in enumerate(lista):
        return f"{numero + 1} ---> {llave["nombre"]},{llave["tipo"]}"
    
def seleccionar_animal(id,lista):
    if id in range (1,11):
        animal_selec = lista[id - 1]
        for key in animal_selec.keys():
            return f"{key} ---> {animal_selec[key]}"
    else:
        print("Elemento inválido")

def filtro(tipo,lista):
    for i in lista:
        if tipo in i.values():
            return f"El animal {i["nombre"]} es un {i["tipo"]}"
        
def agregar_animal(nombre,type,weight,color,lista):
    lista.append({"nombre":nombre,"tipo":type,"peso":weight,"color":color})
    return f"El animal {nombre} ha sido agregado correctamente"

menu = ["Mostrar lista enumerada de animales y seleeccionar uno", "Obtener un animal según su tipo", "Agregar un animal a la lista", "Salir"]
for numero, accion in enumerate(menu):
        print(f"{numero + 1} --> {accion}")

contador = 0

while True:
    eleccion = input("Qué acción desea realizar?: ")
    if eleccion == "1":
        print(lista_enumerada(lista_animales))
        animal = int(input("Ingrese el ID del animal: "))
        print(seleccionar_animal(animal,lista_animales))
        continue
    elif eleccion == "2":
        tipo = input("Ingrese el tipo de animal: ")
        print(filtro(tipo,lista_animales))
        continue
    elif eleccion == "3":
        print("Ingrese su nuevo animal") #nuevo animal
        nombre = input("Ingrese el nombre del animal: ").lower()
        tipo = input("Ingrese el tipo de animal: ")
        peso = int(input("Ingrese el peso del animal en Kg: "))
        color = input("Ingrese el color del animal: ")
        print(agregar_animal(nombre,tipo,peso,color,lista_animales))
        print(lista_animales[-1])
    elif eleccion == "4": #condicion de salida
        print("Hasta pronto!")
        break
    else:
        print("Ingrese una acción válida") #condicion de que el usuario ingrese un número fuera del menú o un caracter inválido
        continue

        

