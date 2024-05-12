import random
from random import randint
hexa="0123456789abcdef"
final_hexa=[]
final_rgb=[]
list_hexa=[]
list_rgb=[]
def generate_colors(name,number):
    if name == "hexa":
        for m in range (0,number):
            for i in range (0,6):
                nueva=random.choice(hexa)
                list_hexa.append(nueva)
                x = "".join(list_hexa)
                print(x)
            final_hexa.append(x)
        return tuple(final_hexa)
    elif name == "rgb":
        for m in range (0,number):
            for i in range (0,3):
                a = randint(0,255)
                list_rgb.append(a)
                x = "".join(str(list_rgb))
            final_rgb.append(x)
        return tuple(final_rgb)
        
print(generate_colors("rgb",2))