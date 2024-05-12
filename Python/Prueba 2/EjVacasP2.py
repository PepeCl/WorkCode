nombres_vacas = [
    "Juan Daniel",
    "Achraf",
    "Jessica",
    "Bernardo",
    "Rosario",
    "Alexis",
    "Ariana",
    "Sacramento",
    "Patrocinio",
    "Patroclo",
    "Viviana",
    "Aroa",
    "Remedios",
    "Luis",
    "David",
    "Urko",
    "Rosa",
    "Isabel",
    "Gael",
    "Josep",
    "Oriol",
    "Maria",
    "Josefa",
    "Elsa",
]
id_vacas = [] #lista para id de vacas
vacas_selec_1 = [] #lista para vacas preselecccionadas
vacas_final = [] #lista final de vacas seleccionadas

letra = input("Ingrese una letra: ")
for i in nombres_vacas:
    if letra in i.lower(): #convierto el nombre a minuscula
        id_vacas.append(nombres_vacas.index(i)+1) #agrego el index + 1 de la vaca a una lista de vacas enumeradas
        vacas_selec_1.append(i) #agrego la vaca que tiene la letra a una lista preliminar de vacas
        print(nombres_vacas.index(i)+1,i) #imprimo el index + 1 de cada vaca y su nombre correspondiente
while True:
    vaca_seleccion = input("Ingrese el id de la vaca a seleccionar: ")
    if vaca_seleccion == "salir": #condicion de salida
        break
    elif (vaca_seleccion.isdigit()): #verifico que sea un numero
        if (int(vaca_seleccion) not in id_vacas): #si el numero no está en la lista de id entonces pido otro número
            print("Id de vaca no reconocido, seleccione una vaca válida")
            continue #vuelvo al ciclo
        else: #condicion de agregar vacas a la lista
            print(f"La vaca {vacas_selec_1[id_vacas.index(int(vaca_seleccion))]} ha sido seleccionada") #muestro el nombre de la vaca
            vacas_final.append(vacas_selec_1[id_vacas.index(int(vaca_seleccion))]) #agrego la vaca seleccionada a una lista final
            continue
    else:
        print("Ingrese un número válido")

print(vacas_final)

#el comando lista.index(n) me devuelve la posición del elemento n en la lista
#como la posicion comienza en 0 debo sumar 1 para comenzar con la enumeración real (ver linea de codigo 34)
# el comando vacas_selec_1[id_vacas.index(int(vaca_seleccion))] realiza la siguiente secuencia
#primero va a la lista de id_vacas y obtiene la posicion del número que ingresa el usuario en la lista de id
#por ejemplo si mi lista de id es id_vacas = [1,2,19,25]
#al escribir id_vacas.index(25) me devuelve la posición del número 25 en la lista
#en este caso el output sería id_vacas.index(25) = 3 (recordar que el conteo comienza en 0)
#ahora, mediante el comando vacas_selec_1[id_vacas.index(int(vaca_seleccion))] puedo obtener el nombre de la vaca 
#en la posición del id seleccionado
#veamos un ejemplo
#vacas_selec_1 = ["Pedro","Luis"]
#id_vacas = [15,19]
#si quiero sacar la vaca Luis mediante el id numero 19 entonces
#id_vacas.index(19) = 1 (ya que la lista tiene 2 elementos, el 0 y el 1)
#vacas_selex_1[1] = Luis
#por lo tanto el comando se vería así vacas_selec_1[id_vacas.index(19)]

                

            