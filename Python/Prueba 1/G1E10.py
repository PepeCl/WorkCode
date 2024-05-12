print("El siguiente programa crea una barra de carga")
x = int(input("ingrese un valor: "))
y = 20
n = x//5
cadena = "*" * n + "-" * (y-n)
print(cadena + "/" + str(x) + "%")