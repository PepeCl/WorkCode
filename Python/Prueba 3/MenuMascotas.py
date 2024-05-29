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
        for i, llave in enumerate(lista_animales):
            print(f"{i + 1} ---> {llave["nombre"]}, {llave["tipo"]}")
        seleccion = int(input("Seleccione el animal: "))
        if seleccion in range (1,11): #condicion de rango de lista
            animal_seleccionado = lista_animales[seleccion-1]
            for key in animal_seleccionado.keys():
                print(f"{key} ---> {animal_seleccionado[key]}")
            continue
        else:
            print("Elemento inválido")
            continue
    elif eleccion == "2":
        filtro  = input("Que tipo de animal desea obtener?: ").lower()
        for i in lista_animales:
            if filtro in i.values():
                contador += 1
                print(f"el animal {i["nombre"]} es un {i["tipo"]}")
        print(f"hay {contador} animales de ese tipo")
        contador = 0
        continue
    elif eleccion == "3":
        print("Ingrese su nuevo animal")
        nombre = input("Ingrese el nombre del animal: ").lower()
        tipo = input("Ingrese el tipo de animal: ")
        peso = int(input("Ingrese el peso del animal en Kg: "))
        color = input("Ingrese el color del animal: ")
        lista_animales.append({"nombre":nombre,"tipo":tipo,"peso":peso,"color":color})
        print(f"El animal de nombre {nombre} ha sido agregado correctamente a su lista")
        print(lista_animales[-1])
        print(input( ))
        continue
    elif eleccion == "4":
        print("Hasta pronto!")
        break
    else:
        print("Ingrese una acción válida")
        continue