import random
import string

def random_user_id():
    largo_clave=int(input("Ingrese la longitud que desea que tenga su clave: "))
    numero_id=int(input("Que cantidad de claves desea generar?: "))
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits
    
    # Generate a six-character random user ID
    for i in range (0, numero_id):
        user_id = "".join(random.choices(characters, k=largo_clave)) #con el comando k=x defino el largo del string de choices. si no uno con "".join me devuelve una lista.
        print(user_id)

# Test the function
random_user_id()
