"""
Un grupo de científicos le pasa una lista con secuencias de ADN.

Cada secuencia es un texto que tiene las letras 'A 'T 'C o 'G

Las letras siempre deben ir en pares que son AT o TA o CG o GC, todas separadas por un -

Usted debe crear un programa que lea esta lista de cadenas de ADN e indique cuál de estas cadenas es una secuencia válida y cuál no.

Considere que la secuencia solo contendrá letras y el -, estará bien escrita.

ej cadenas:

 AT-CG-GC-GC-AT => BIEN

 AT-TC-TA => MAL

Ejemplo de lista

adn = [

'AT-CG-GG-TA-TA-TT',

'AA-AT-CG-GC-GC-TA-AT',

'AT-TA-GC',

]

resultado:

MALO

MALO

BUENO

"""

adn = [

'AT-CG-GG-TA-TA-TT',

'AA-AT-CG-GC-GC-TA-AT',

'AT-TA-GC',

"perro"

]

perro = ["asdasd","asadqweqw"]

correctas = ["AT","TA","CG","GC"]

def secuencia_adn(lista):
    contador = True
    lista_adn = []
    for cadena in lista:
        nueva_lista = cadena.split("-")
        lista_adn.append(nueva_lista)
    for alfa in lista_adn:
        for dna in alfa:
            if dna not in correctas:
                contador = False
        if contador == True:
            print("correctas")
        else:
            print("Incorrecta")
        contador = True
       
secuencia_adn(adn)


