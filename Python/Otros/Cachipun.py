import random
print("Bienvenido al CACHIPUN!!!")
cpu = ["Piedra","Papel","Tijeras"]
while True:
    usuario = input("Ingresa que quieres sacar (Piedra/Papel/Tijeras): ").capitalize()
    if usuario not in cpu:
        print("Ingresa un movimiento válido")
        break
    else:
        cpu_mov = random.choice(cpu)
        print(cpu_mov)
        if cpu_mov == "Piedra":
            if usuario == "Piedra":
                print("Empate")
            elif usuario == "Papel":
                print("Haz ganado!")
            elif usuario == "Tijeras":
                print("Haz perdido :c")
        if cpu_mov == "Papel":
            if usuario == "Piedra":
                print("Haz perdido :c")
            elif usuario == "Papel":
                print("Empate")
            elif usuario == "Tijeras":
                print("Haz ganado!")
        if cpu_mov == "Tijeras":
            if usuario == "Piedra":
                print("Haz ganado!")
            elif usuario == "Papel":
                print("Haz perdido :c")
            elif usuario == "Tijeras":
                print("Empate")
    