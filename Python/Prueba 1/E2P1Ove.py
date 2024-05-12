color=input("De qué color es la oveja?: ").lower()
peso=float(input("Cuánto pesa tu oveja? [kg]: "))
tamano=float(input("De qué tamaño es tu oveja? [cm]: "))
precio_oveja = 0
if peso >= 60:
    precio_oveja = precio_oveja + 1500
elif peso < 60:
    precio_oveja = precio_oveja + 1000
if color == "negro":
    precio_oveja = precio_oveja + 100
elif color == "morado":
    precio_oveja = precio_oveja + 200
elif color == "ocre":
    precio_oveja = precio_oveja + 150
if tamano > 60 and tamano <=100:
    precio_oveja = precio_oveja + 1.5*tamano
elif tamano > 100:
    precio_oveja = precio_oveja + 1000
print("Tu oveja tiene un precio adicional de:", precio_oveja)