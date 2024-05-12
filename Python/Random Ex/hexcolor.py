import random
mylist=("0123456789abcdef")
new_list=[]

def list_of_hexa_colors():
    for i in range (0,6):
        rdm=random.choice(mylist)
        new_list.append(rdm)
    return "".join(new_list)

print(f"#{list_of_hexa_colors()}")
        
