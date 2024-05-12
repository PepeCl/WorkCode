from random import randint
rgb=[]

def rgb_color_gen():
    for i in range (0,3):
        a=randint(0,255)
        rgb.append(a)
    return(tuple(rgb))

print(rgb_color_gen())
        