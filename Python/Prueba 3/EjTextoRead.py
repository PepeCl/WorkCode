nombre_archivo = "mi_archivo.txt"

with open(nombre_archivo,"r") as archivo:
    while True:
        linea = archivo.readline()
        print(type(linea))
        if not linea:
            break
        print(linea,end="")


with open(nombre_archivo,"r") as archivo:
    lineas = archivo.readlines()
    print(type(lineas))
for linea in lineas:
    print(linea,end="")