A = input("Cual es el estado de A? ON / OFF: ").upper()
B = input("Cual es el estado de B? ON / OFF: ").upper()
C = input("Cual es el estado de C? ON / OFF: ").upper()
D = input("Cual es el estado de D? ON / OFF: ").upper()
puerta = "Abierta"
if B == "ON" and A == C == D == "OFF":
    puerta = "Cerrada"
    print("La puerta está",puerta)
else:
    print("La puerta está",puerta)