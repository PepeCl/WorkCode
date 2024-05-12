print("El siguiente programa crea un cronómetro de cuenta regresiva")
import time
from os import system
import winsound
x = int(input("Ingrese el tiempo que desea: "))
frequency = 660  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
y = 0.3
system("cls")
while x != 0:
    print("Quedan " + str(x) + " [seg]")
    winsound.Beep(frequency, duration)
    x = x - 1
    time.sleep(y)
    system("cls")
print("Se ha acabado el tiempo")
winsound.Beep(1000,2000)



