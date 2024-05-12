nombre_1 = input("Nombre del comprador 1: ")
medicamento_1 = input("Medicamento a comprar: ").lower()
cantidad_1 = int(input("Qué cantidad de medicamento desea comprar?: "))
sintoma_1 = input("Qué sintomas tiene (Dolores/Infección/Hipertensión)?: ").lower()

nombre_2 = input("Nombre del comprador 2: ")
medicamento_2 = input("Medicamento a comprar: ").lower()
cantidad_2 = int(input("Qué cantidad de medicamento desea comprar?: "))
sintoma_2 = input("Qué sintomas tiene (Dolores/Infección/Hipertensión)?: ").lower()


nombre_3 = input("Nombre del comprador 3: ")
medicamento_3 = input("Medicamento a comprar: ").lower()
cantidad_3 = int(input("Qué cantidad de medicamento desea comprar?: "))
sintoma_3 = input("Qué sintomas tiene (Dolores/Infección/Hipertensión)?: ").lower()

los1=0
los2=0
los3=0

precio_pen3=0
precio_pen2=0
precio_pen1=0

precio_asp1=0
precio_asp2=0
precio_asp3=0

precio_los1=0
precio_los2=0
precio_los3=0

total_1=0
total_2=0
total_3=0

if medicamento_1 == "aspirina" and sintoma_1 == "dolores":
    precio_asp1 = 300 * cantidad_1
    total_1=precio_asp1
elif medicamento_1 == "penicilina" and sintoma_1 == "infeccion":
    precio_pen1 = 2000 * cantidad_1
    total_1=precio_pen1
elif medicamento_1 == "losartan" and sintoma_1 == "hipertension":
    precio_los1 = 400 * cantidad_1
    los1=cantidad_1
    total_1=precio_los1
else:
    print("No puede comprar ninguna medicina")

if medicamento_2 == "aspirina" and sintoma_2 == "dolores":
    precio_asp2 = 300 * cantidad_2
    total_2=precio_asp2
elif medicamento_2 == "penicilina" and sintoma_2 == "infeccion":
    precio_pen2 = 2000 * cantidad_2
    total_2=precio_pen2
elif medicamento_2 == "losartan" and sintoma_2 == "hipertension":
    precio_los2 = 400 * cantidad_2
    los2=cantidad_2
    total_2=precio_los2
else:
    print("No puede comprar ninguna medicina")

if medicamento_3 == "aspirina" and sintoma_3 == "dolores":
    precio_asp3 = 300 * cantidad_3
    total_3=precio_asp3
elif medicamento_3 == "penicilina" and sintoma_3 == "infeccion":
    precio_pen3 = 2000 * cantidad_3
    total_3 = precio_pen3
elif medicamento_3 == "losartan" and sintoma_3 == "hipertension":
    precio_los3 = 400 * cantidad_3
    total_3=precio_los3
    los3=cantidad_3
else:
    print("No puede comprar ninguna medicina")

if total_1 > total_2  and total_1> total_3:
    gastador = nombre_1
elif total_2 > total_1 and total_2 > total_3:
    gastador = nombre_2
elif total_3 > total_1 and total_3 > total_2:
    gastador = nombre_3

total_los = los1 + los2 + los3
total_din= total_1 + total_2 + total_3
total_pen= precio_pen1 + precio_pen2 + precio_pen3



print(f"Se vendieron {total_los} Losartan")
print(f"El total del dinero recaudado es ${total_din}")
print(f"El nombre de la persona que más gastó es {gastador}")
print(f"El total recaudado en penicilina fue: ${total_pen}")






