import time
x = input("Ingrese un número: ")
if x.isdigit():
   print("Adios, me voy luego de " + str(x) + " " + "segundos")
   time.sleep(int(x))
else:
   print("Ingrese un número válido")