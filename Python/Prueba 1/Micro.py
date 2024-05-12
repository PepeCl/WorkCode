print("El siguiente programa te muestra si puedes llegar a tu destino")
distancia=float(input("Ingrese la distancia en metros [m]: "))
micro = input("Tienes alguna micro cerca?: ").capitalize()
metro = input("Existe algún metro cerca de tu casa?: ").capitalize()
if distancia <=500:
    print("Puedes llegar caminando a tu destino")
elif (distancia > 500 and distancia < 1500):
    if metro == "Si" or micro == "Si":
        print(micro, "puedes usar micro para llegar")
        print(metro, "puedes usar metro para llegar")
    else:
        print("No puedes llegar bajo las condiciones de transporte dadas")
elif distancia >= 1500:
    if metro == "Si" and micro == "Si":
        print("Vives muy lejos ! Necesitas tomar micro y metro para llegar")
    else:
        print("No puedes llegar bajo las condiciones de transporte dadas")