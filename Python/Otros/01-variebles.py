lista = ["AT-CG-TT","CG-AT-GG"]
lista_adn=[]
for i in lista:
    nueva_lista = i.split("-")
    lista_adn.append(nueva_lista)
print(lista_adn)