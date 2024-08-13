def latencia_real(tiempo):
    return tiempo * 1.2

latencia_estimada_1 = 200
latencia_estimada_2 = 149
latencia_estimada_3 = 74

print(f"La latencia real de {latencia_estimada_1} [ms] es igual a: {latencia_real(latencia_estimada_1)} [ms]")
print(f"La latencia real de {latencia_estimada_2} [ms] es igual a: {latencia_real(latencia_estimada_2)} [ms]")
print(f"La latencia real de {latencia_estimada_3} [ms] es igual a: {latencia_real(latencia_estimada_3)} [ms]")