dia_semana=input("Ingrese el día de la semana que tiene disponible: ").lower()
edad=int(input("Ingrese su edad: "))
dinero=int(input("Ingrese el dinero que tiene: $"))
Barrio_italia = "No"
Bellavista = "No"
Valparaiso = "No"
After = "No"
Happyland = "No"
if edad >=13:
    if dia_semana in ("lunes,martes,miercoles,jueves,viernes,sabado,domingo"):
        if dinero >= 1000:
            Happyland = "Si"
if edad >= 18:
    if dia_semana in ("lunes,martes,miercoles,jueves,viernes,sabado,domingo"):
        if dinero >= 0 and dia_semana in ("sabado,domingo"):
            Valparaiso = "Si"
        if dinero >= 1000:
            Bellavista = "Si"
        if dinero >= 4000 and dia_semana in ("jueves,viernes,sabado,domingo"):
            Barrio_italia = "Si"
if edad >= 25:
    if dia_semana in ("jueves,viernes,sabado"):
        if dinero >= 6000:
            After = "Si" 
print("Puedes ir a:\n Bellavista", Bellavista, "\n Barrio Italia", Barrio_italia, "\n Valparaiso", Valparaiso , "\n After Office", After, "\n HappyLand", Happyland)

# dia_valparaiso = (lasinaslk,aksjdjas)
