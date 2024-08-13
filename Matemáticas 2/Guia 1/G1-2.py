def transmision_datos(segundos):
    return 100*segundos

for tiempo in range (0,1001,100):
    print(f"En {tiempo} [seg] se transmiten {transmision_datos(tiempo)} megabits")
