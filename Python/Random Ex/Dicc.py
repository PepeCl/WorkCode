diccionario = {"Nombre" : "Giuseppe Saavedra", "Nacimiento":"Quinta Normal","Vive en":"Ñuñoa" , "Novia":"Tatiana Contreras", "Hijo":"Nino"}
print(diccionario.keys()) #llama a las llaves

#agregar elementos a un diccionario
#diccionario[elemento que quiero que sea la nueva llave]=Elemento que quiero agregar
#ej

diccionario["Madre"]="Alejandra Chávez"
print(diccionario)

#se agrega al final del diccionario

diccionario["Hijo"]="Perro Nino"
print(diccionario)

#con esta forma modificamos el contenido de una llave

del diccionario["Nombre"]
print (diccionario)

#se borra el contenido de la llave puesta

#del diccionario["Giuseppe Saavedra"] #SOLO ELIMINA LLAVES, NO CONTENIDO INDEXADO
#print(diccionario)

print(diccionario.items())
