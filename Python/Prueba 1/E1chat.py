numero = int(input("Ingrese un número del 1 al 10: "))
es_par = numero % 2
if numero > 10:
    print ("Número no válido")
if es_par == 0:
    for i in range (2, numero + 1 ,2):
        print(i)
else:
    for i in range (1, numero + 1 ,2):
        print(i)
        
