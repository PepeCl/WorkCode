
def iteracion(n,m):
    for i in range (1,3):
        n = i+n
        m = 2*i+m
        print(n)
        print(m)
    return n + m

resultado = iteracion(5,4) #asigno resultado a variable
print(resultado) #llamo nueva variable
