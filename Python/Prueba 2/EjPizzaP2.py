lista_pizzas = ["Tradicional","Pepperoni","Margarita","Napolitana","Carnes"]
lista_precios = [12000,14000,12500,11000,17000]

for i in range (len(lista_pizzas)):
    print(f"{lista_pizzas[i]} = ${lista_precios[i]}")

usuarios = [] #almacena usuarios
tipo_usuarios = [] #almacena si el usuario es estudiante o profesor
lista_compras = [] #almacena las compras de cada usuario
lista_usuarios = [] #almacena una lista de compras de todos los usuarios
suma_pizza = 0 #suma el consumo de cada usuario
lista_suma=[] #lista de consumo de todos los usuarios

while True:
    nombre = input("Ingresa tu nombre (Para salir escribe 'salir'): ")
    if nombre == "salir":
        break
    else:
        usuarios.append(nombre)

    tipo = input("Qué tipo de usuario eres? Estudiante / Profesor: ")
    tipo_usuarios.append(tipo)

    while True:
        pizza = input("Qué pizza deseas comprar? (Para salir escribe 'salir'): ").lower()
        if pizza == "salir":
            lista_compras.append(lista_usuarios) #agrego cada pizza a una lista de pizza
            break
        else:
            lista_usuarios.append(pizza) #agrego cada lista de pizza a una lista total de usuarios
    lista_usuarios = []

for i in lista_compras: #suma pizzas por usuario
    for j in i:
        if j == "tradicional":
            suma_pizza += 12000
        elif j == "pepperoni":
            suma_pizza += 14000
        elif j == "margarita":
            suma_pizza += 12500
        elif j == "napolitana":
            suma_pizza += 11000
        elif j == "carnes":
            suma_pizza += 17000
    lista_suma.append(suma_pizza) #lista de consumo por usuario
    suma_pizza = 0 #hago 0 la suma para que almacene el consumo de cada usuario

for i in lista_compras:
    if (i.count("napolitana")) == 3: #condicion de descuento por cantidad
        lista_suma[lista_compras.index(i)] -= 11000
    elif (i.count("pepperoni")) == 2:
        lista_suma[lista_compras.index(i)] = lista_suma[lista_compras.index(i)] * 0.9

for i in tipo_usuarios:
    if i == "estudiante": #condicion de descuento por tipo de usuario
        lista_suma[tipo_usuarios.index(i)] = lista_suma[tipo_usuarios.index(i)] * 0.8
    elif i == "profesor":
        lista_suma[tipo_usuarios.index(i)] = lista_suma[tipo_usuarios.index(i)] * 0.9

for i in range(len(usuarios)):
    print(f"El usuario {usuarios[i]} ha consumido un total de = ${lista_suma[i]}") #imprimo cada usuario y su consumo total     





