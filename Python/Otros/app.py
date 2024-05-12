x=int(input("Ingresa un número: "))
ans = 0
while ans**3<abs(x):
    ans+=1
if ans**3 != abs(x):
    print(str(x) + " no es un cubo perfecto")
else:
    if x < 0:
        ans = str(abs(ans)) + " i" 
    print ("La raíz cubica de " + str(x) + " es " + str(ans))