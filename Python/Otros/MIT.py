while True:
    palabra=input("ingrese una palabra:")
    inversa=palabra[::-1]
    if palabra == "salir":
        break
    if palabra == inversa:
        print("Tu palabra es un palindromo")
    else:
        print("Tu palabra no es un palindromo")
        