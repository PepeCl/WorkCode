mes_anterior = str(input("Que alimento compro el mes anterior? ")).lower() #paso el str a minusculas

if "gato" in mes_anterior or "perro" in mes_anterior: #creo la condición de que la palabra gato o perro debe estar en el string inicial, en el caso que no esté inmediatamente salta a que no tiene ese animal
    gatos = int(input("Cuantos gatos tiene?: "))
    perros = int(input("Cuantos perros tiene?: "))
    iguanas = int(input("Cuantas iguanas tiene?: "))
    rinocerontes = int(input("Cuantos rinocerontes tiene?: "))

    if (gatos > perros and "gato" not in mes_anterior): #condicion de cantidad de gatos vs perros y que dentro del string mes anterior NO esté contenida la palabra GATO
        alimento = (10*gatos + 2*iguanas)
        print("Puedes comprar alimento de gato", alimento, "kg")

    elif (perros > gatos and "perro" not in mes_anterior): #condicion de cantidad de gatos vs perros y que dentro del string mes anterior NO esté contenida la palabra PERRO
        alimento = 15*perros + 3*rinocerontes
        print("Puedes comprar alimento de perro", alimento, "kg")

    elif (perros == gatos): #no necesita compra de alimento en el mes anterior, solo igualdad de cantidad de animales
        alimento = 10*iguanas + 3*rinocerontes
        print("Puedes comprar alimento de iguana", alimento, "kg")
    else:
        print("No puedes comprar ningún alimento")
else:
    print("No tengo ese animal")



