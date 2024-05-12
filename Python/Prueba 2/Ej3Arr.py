cont_vocales = 0
vocales = "aeiou"
texto = input("Ingrese un texto completo: ")
for i in texto:
    if i in vocales:
        cont_vocales += 1
print(cont_vocales)