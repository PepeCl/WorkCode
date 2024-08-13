def transmision_datos(segundos):
    return 100*segundos

tiempo_1 = 45
tiempo_2 = 1.5*60
tiempo_3 = 1*60*60

print(f"En 45 [seg] se transmiten {transmision_datos(tiempo_1)} megabits")
print(f"En 1.5 [min] se transmiten {transmision_datos(tiempo_2)} megabits")
print(f"En 1 [hr] se transmiten {transmision_datos(tiempo_3)} megabits")
