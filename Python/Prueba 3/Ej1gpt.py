def analisis_de_texto(texto):
    dict_palabras = {}
    lista_texto = texto.split(" ")
    for palabras in lista_texto:
        dict_palabras[palabras] = lista_texto.count(palabras)
    for frecuencias in dict_palabras.values():
        print(frecuencias)


    return dict_palabras



analisis_de_texto("habia una vez un perrito llamado nino que vivia en ñuñoa ñuñoa nino nino perro perrIto")
