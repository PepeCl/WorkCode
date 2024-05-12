lista_pizzas = ["Tradicional","Pepperoni","Margarita","Napolitana","Carnes"]
lista_precios = [12000,14000,12500,11000,17000]

for i in range (len(lista_pizzas)):
    print(f"{lista_pizzas[i]} = ${lista_precios[i]}")

usuarios = []
tipo_usuarios = []
lista_compras = []
lista_usuarios = []

while True:
    nombre = input("Ingresa tu nombre (Para salir escribe 'salir'): ")
    if nombre == "salir":
        break
    else:
        usuarios.append(nombre)

    tipo = input("Qué tipo de usuario eres? Estudiante / Profesor: ")
    tipo_usuarios.append(tipo)

    while True:
        pizza = input("Qué pizza deseas comprar?: ").lower()
        if pizza == "salir":
            lista_compras.append(lista_usuarios)
            print(lista_compras)
            break
        else:
            lista_usuarios.append(pizza)
            print(lista_usuarios)
    lista_usuarios = []

for i in lista_compras:
    print (i)


print(usuarios)
print(tipo_usuarios)
print(lista_compras)




