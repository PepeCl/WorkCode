lista_frutas = ["Manzana","Tomate","Limon","Sandia","Naranja"]
lista_de_precios = [1500,3000,700,7000,800]
frutas_recolectadas = []
peso_por_fruta = []
frutas_venta = []
precio_venta = []
precio = 0

for i in range (len(lista_frutas)):
    print(f" Kg de {lista_frutas[i]} = ${lista_de_precios[i]}") #despliegue de frutas con su precio respectivo
while True:
    frutas = input("Ingrese la fruta recolectada (para salir escriba 'salir'): ").lower()
    if frutas == "salir": #condicion de salida
        break
    else:
        frutas_recolectadas.append(frutas) #agrego frutas a lista de frutas recolectadas
    peso = float(input("Ingrese el peso recolectado en Kg: "))
    peso_por_fruta.append(peso) #agrego peso a lista de pesos de cada fruta


for i in range (len(frutas_recolectadas)): #recorro la lista de frutas recolectadas 
    if frutas_recolectadas[i] == "manzana":
        precio = lista_de_precios[0] * peso_por_fruta [i] #se multiplica el valor de la fruta respectiva con el peso correspondiente
    elif frutas_recolectadas[i] == "tomate":
        precio = lista_de_precios[1] * peso_por_fruta [i]
    elif frutas_recolectadas[i] == "limon":
        precio = lista_de_precios[2] * peso_por_fruta [i]
    elif frutas_recolectadas[i] == "sandia":
        precio = lista_de_precios[3] * peso_por_fruta [i]
    elif frutas_recolectadas[i] == "naranja":
        precio = lista_de_precios[4] * peso_por_fruta [i]
    else: #si la fruta no está en la lista de frutas el programa no hace nada y pasa a la siguiente iteracion
        continue
    precio_venta.append(precio) #agrega el precio a una lista de precios


for i in range (len(frutas_recolectadas)):
    if frutas_recolectadas[i].capitalize() in lista_frutas: #comando .capitalize() para convertir la primera letra en mayuscula, ya que la lista de frutas está escrita así
        frutas_venta.append(frutas_recolectadas[i]) #si la fruta recolectada está en la lista de frutas a la venta entonces se agrega a una lista final de frutas vendidas      
    else:  #si la fruta no está en la lista de frutas, entonces que pase a la siguiente iteración
        continue

print(f"El precio de venta de cada fruta es")
for i in range (len(frutas_venta)): #despliegue de cada fruta con su respectivo precio de venta
    print(f"{frutas_venta[i].capitalize()} = ${int(precio_venta[i])}")