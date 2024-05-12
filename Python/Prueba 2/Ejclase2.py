letra = input("Ingrese una palabra: ").lower()
contador = 0
for i in letra:
    if i in "aeiou":
        contador += 1
print(contador)
