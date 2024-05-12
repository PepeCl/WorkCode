from os import system
import time
print("Bienvenido al juego del COLGADOOOO !!!!")
palabra = str(input("Qué palabra vamos a adivinar?: ")).lower()
colgado = "_" * len(palabra) #creo un nuevo string con el largo de la palabra pero con _ como caracteres
colgado_mod=list(colgado) #convierto el string anterior a lista para modificarlo caracter por caracter
intentos=5 #numero de intentos, puede cambiar segun se quiera
incorrectas=[] #hago una lista que almacene las letras que no están en la palabra
system("cls") #limpio el sistema para que la otra persona no vea la palabra
print("Comencemos, adivina la palabra")
while True: #entro al bucle
    print(colgado)
    print(f"Tienes {intentos} intentos")
    print(f"Las letras que no contiene la palabra son: {incorrectas}")
    adivina = input("Ingresa una letra: ")
    if len(adivina) == 1:
        for i in range(len(palabra)): #recorro la palabra caracter por caracter
            if palabra[i] == adivina: #si existe coincidencia de letra entonces
                colgado_mod[i] = adivina #modifica en la posición i la letra adivinada
                colgado="".join(colgado_mod) #junto la lista en el string de _
        if adivina not in palabra: #condicion de perdida de intentos
            intentos = intentos - 1
            incorrectas.append(adivina)
        system("cls")
        if palabra == colgado: #condición de ganar
            print(f"La palabra era: {palabra}")
            print("GANASTE !")
            break
        if intentos == 0: #condición de perder
            print(f"La palabra era: {palabra}")
            print("Te has quedado sin intentos disponibles")
            break
    else: #condicion de ingreso erroneo de letras
        print("Debe ingresar sólo 1 letra") 
        time.sleep(1)
        system("cls")
        continue






