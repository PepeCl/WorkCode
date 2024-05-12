nombre =  input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nacimiento = input("Ingrese año de nacimiento: ")
correo = nombre[0] + nombre[2] + "." + apellido[-2] + apellido[-1] + "@duoc.cl"
password = apellido[0] + nacimiento [::-1] + str(len(nombre))
print(correo)
print(password)
