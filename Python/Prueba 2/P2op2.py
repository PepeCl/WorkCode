#suponga que le dan una lsita de varios textos, debe calcular el peso de cada texto
#segun lo siguiente, cada letra tiene un valor
#a=1,b=2,c=3 hasta la z
#las mayusculas valen el doble
#no se consideran ñ ni Ñ
#por cada numero en el texto se suma el valor de ese numero al peso
#hay simbolos que restan valor al peso
# * - & $ gato
# son -1 -2 -3 -5 -10
#el resto de simbolos no afecta en nada
#muestre en pantalla una lista con el peso de cada texto de la lista incial
#la palabra con más valor
#la palabra con menos valor
#el promedio de valor de las palabras
#ejemplo
#texto1 = ab123 ---> 9
#texto2 = a* ---> 0
#texto3 = AaA ---> 5
#lista_final = [AaA,a*,ab123]


def sumador_de_letras(lista1):
    abecedario = list("abcdefghijklmnopqrstuvwxyz")
    caracteres = list("*-&$#")
    sumador = 0
    promedio = 0
    palabra_mas_pesada = ""
    palabra_menos_pesada = ""
    lista_sumador = []
    for i in lista1:
        for j in i:
            if j in abecedario:
                sumador += (abecedario.index(j)+1)
            elif j.isupper():
                j = j.lower()
                sumador += ((abecedario.index(j)+1)*2)
            elif j.isdigit():
                j = int(j)
                sumador += j
            elif j in caracteres:
                if j == "*":
                    sumador -= 1
                elif j == "-":
                    sumador -= 2
                elif j == "&":
                    sumador -= 3
                elif j == "$":
                    sumador -= 5
                elif j == "#":
                    sumador -= 10
        lista_sumador.append(sumador)
        sumador=0

    palabra_mas_pesada = lista1[lista_sumador.index(max(lista_sumador))]
    palabra_menos_pesada = lista1[lista_sumador.index(min(lista_sumador))]
    
    for i in lista_sumador:
        sumador += i
    promedio = (sumador/len(lista_sumador))
    


    return f"La lista de pesos es {lista_sumador}\nla palabra más pesada es {palabra_mas_pesada}\nla palabra menos pesada es {palabra_menos_pesada}\nel promedio de las palabras es {promedio}"
    



lista_1 =["AaA","a*","ab123"]
print(sumador_de_letras(lista_1))        

            
        

