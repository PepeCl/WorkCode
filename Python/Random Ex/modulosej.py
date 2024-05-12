import random
import string

def random_user_id():
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits
    
    # Generate a six-character random user ID
    user_id = "".join(random.choices(characters, k=6)) #con el comando k=x defino el largo del string de choices. si no uno con "".join me devuelve una lista.
    
    return user_id

# Test the function
print(random_user_id())
