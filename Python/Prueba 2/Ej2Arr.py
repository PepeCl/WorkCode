lista =[]
vocales = "aeiou"
cont_largo = 0
cont_vocales = 0
cont_voc2=0
mas_larga = ""
mas_vocales = ""
while True:
    palabra = input("Ingrese una palabra: ")
    if palabra == "salir":
        break
    else:
        lista.append(palabra)
for i in lista:
    if (len(i)>cont_largo):
        mas_larga = i
for i in lista:
    for j in i:
        if j in vocales:
            cont_vocales +=1
        if cont_vocales > cont_voc2:
            cont_voc2 = cont_vocales
            mas_vocales = i
print(mas_larga)
print(mas_vocales)

            





