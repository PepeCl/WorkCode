"""
Sumador de letras

   Supongamos que le dan una lista de varios textos, debe calcular el peso de cada texto segun lo siguiente:
   Se asigna un valor a cada letra, de la siguiente manera:

   a = 1, b = 2, c = 3 ... hasta la z
   Puede considerar que no se ingresan "ñ" o "Ñ"

   Por cada numero en el texto, se suma el valor de ese numero al "peso".

   Hay simbolos que restan valor al "peso".
   * = -1, - = -2, & = -3, $ = -5, # = -10
   El resto no afecta nada.

Muestre en pantalla una lista con el peso de cada texto de la lista inicial.
La palabra con mas valor
La palabra con menor valor
El promedio de valor de las palabras.

Ejemplo:
texti1 = "ab123" --> 9
texti2 = "a*" --> 0
texto3 = "AaA" --> 5

OUTPUT = ["ab123", "AaA", "A*"]
"""
diccionario_letras = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 2, 'B': 3, 'C': 4, 'D': 5, 'E': 6, 'F': 7, 'G': 8, 'H': 9, 'I': 10, 'J': 11,
    'K': 12, 'L': 13, 'M': 14, 'N': 15, 'O': 16, 'P': 17, 'Q': 18, 'R': 19, 'S': 20,
    'T': 21, 'U': 22, 'V': 23, 'W': 24, 'X': 25, 'Y': 26, 'Z': 27
} # Diccionario para almacenar los datos y valor de cada letra.   no supe como hacer para que la mayuscula de cada una tenga un +1 en ella, por eso esta echo de esta forma.

simbolos_operaciones = {
    '*': -1, '-': -2, '&': -3, '$': -5, '#': -10
}

lista_textos = [] # Lista para almacenar el texto a ingresar o ingresado
print("Ingrese textos uno a uno. Escriba 'fin' para terminar la entrada.")

while True:  # ciclo para poder ingresar datos hasta que se ingrese la palabra 'fin'
    texto = input("Ingrese un texto: ")
    if texto.lower() == 'fin':
        break
    lista_textos.append(texto.strip()) # texto.strip() lo uso para eliminar los espacios en blanco al inicio y al final de la frase que son innecesarios.

# Variables
pesos = []
max_peso = float('-inf')
min_peso = float('inf')
suma_pesos = 0
texto_maximo = ""
texto_minimo = ""

for texto in lista_textos:
    peso = 0
    for frase in texto:
        if frase in diccionario_letras:
            peso += diccionario_letras[frase]
        elif frase.isdigit(): # Para saber si es un numero o no.
            peso += int(frase)
        elif frase in simbolos_operaciones:
            peso += simbolos_operaciones[frase]
    pesos.append(peso)
    suma_pesos += peso

    # Actualizar máximo y mínimo
    if peso > max_peso:
        max_peso = peso
        texto_maximo = texto
    if peso < min_peso:
        min_peso = peso
        texto_minimo = texto

promedio_peso = suma_pesos / len(lista_textos) if lista_textos else 0  #Calculo del promedio

print("Pesos de cada texto:", list(zip(lista_textos, pesos)))  # list ayuda a poder imprimir los datos del diccionario en forma de tupla y el zip ayuda a que se vea de mejor manera cada dato con su respectivo resultado
print("Texto con más valor:", texto_maximo)
print("Texto con menor valor:", texto_minimo)
print("Promedio de valor de los textos:", promedio_peso)