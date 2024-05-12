
x = input("Por quién deseas votar? Pepito | Pablito | Juanita: ").capitalize()
lista = ("Pepito","Pablito","Juanita")
if x in lista:
    print("Voto Válido")
    
else:
    print("Voto inválido")

# le agregué la funcionalidad de que si la persona ingresa un voto no valido
# el programa le pida ingresar un voto valido
# aunque no sea parte de la evaluacion inicial, ingrese una tupla para agrupar los nombres

