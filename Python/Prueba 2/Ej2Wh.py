string = ""
verifica = ""

while True:
    letras = input("Ingrese una letra: ").lower
    if len(letras) == 1:
        string = string + letras
        verifica = letras
        if len(string)==1:
            continue
        elif verifica == string[-2]:
            break
    else:
        print("Ingrese solo UNA letra")
        continue 
print(string)

