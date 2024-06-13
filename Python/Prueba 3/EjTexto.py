nombre_archivo = "mi_archivo.txt"
contenido = """Habia una vez un perro llamado nino.
Este perro vivia en ñuñoa
Un día comió 2 desayunos.
"""

with open(nombre_archivo,"w") as archivo:
    archivo.write(contenido)

