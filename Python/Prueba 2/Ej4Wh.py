print("Bienvenido al juego 'Cadena de Palabras'")
print("Instrucciones:")
print("Debe ingresar una palabra que comience con la última letra de la palabra anterior")
print("La primera palabra para este nivel es JUEGO")
anterior = "Juego"
while True:
    palabra = input("Ingrese una palabra: ")
    if palabra.isalpha() == False: #verifica si todas los caracteres del string son letras
        print("Ingrese una palabra correcta")
        continue
    if palabra[0] == anterior[-1]:#comparo la primera letra con la ultima
        anterior = palabra #almaceno la nueva palabra
        print(f"La palabra ahora es: {anterior}")
        continue
    else:
        print("Perdiste :/")
        break