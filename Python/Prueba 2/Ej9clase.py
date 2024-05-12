lista_num = [31,28,31,30,31,30,31,31,30,31,30,31]
lista_mes = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
while True:
    numero = int(input("Ingrese un número del mes: "))
    if numero > 12:
        print("Ingrese un número de un mes válido")
        continue
    else:
        print(f"Tu mes es {lista_mes[numero - 1]} y tiene {lista_num[numero -1]} días")
        break
    