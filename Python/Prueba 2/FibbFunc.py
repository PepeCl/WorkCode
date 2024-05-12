def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci (n-2)

numero = int(input("Ingrese un número: "))
for i in range (numero):
    if fibonacci(i) > numero:
        break
    print(fibonacci(i))