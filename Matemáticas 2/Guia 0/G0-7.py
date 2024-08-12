def conversor_f_to_c(celcius):
    fahrenheit = (9/5) * celcius +32
    return fahrenheit

print(conversor_f_to_c(30))

temperatura_celcius = float(input("Ingrese la temperatura en grados Celcius (°C): "))

print(conversor_f_to_c(temperatura_celcius))
print(round(conversor_f_to_c(temperatura_celcius)))