def initPkm(nombre:str,tipo:str,especie:str) -> dict:
    nombre_archivo = str(nombre) + "_datos.csv"
    archivo = open(nombre_archivo,"w")
    archivo.write(nombre+"\n")
    archivo.write(tipo+"\n")
    archivo.write(especie+"\n")
    archivo.write("50\n50\n")
    
    archivo.close()

def savePkm(pokemon:dict) -> str:
    nombre_archivo = str(pokemon["nombre"]) + "_datos.csv"
    archivo = open(nombre_archivo,"w")
    archivo.write(pokemon["nombre"]+"\n")
    archivo.write(pokemon["tipo"]+"\n")
    archivo.write(pokemon["especie"]+"\n")
    archivo.write(pokemon["hambre"]+"\n")
    archivo.write(pokemon["felicidad"]+"\n")
    archivo.write("50\n50\n")
    
    archivo.close()

pokemon = {"nombre":"","tipo":"","especie":"","felicidad":0,"hambre":0}

def alimentar(pokemon:dict,comida:int) -> None:
    pokemon["hambre"] -= comida
    if (pokemon["hambre"]<0):
        pokemon["hambre"]=0


