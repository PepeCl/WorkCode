"""
Puede escribir aqui las funciones del codigo
Se importaran de forma automatica al 'main.py'
"""
# ------ NO BORRAR -----
def test () -> None:
    """
        Funcion para probar el archivo
    """
    import herramientas
    menu = herramientas.load_items('menu.csv')
    print(menu)

# esto es para que test solo corra si es ejecutado directamente
if __name__ == '__main__':
    test()
# ------ NO BORRAR -----

#Escribir Funciones desde aqui hacia abajo ------------
carrito_user = []
#ejemplo de funcion
def revisar_menu(lista_menu):
    for comidas in lista_menu:
        print(f"{comidas["nombre"]}---> Precio = {comidas["precio"]}")
    while True:
        opcion = input("Desea agregar alguna comida a su carrito de compras? (s/n): ")
        if opcion == "s":
            item = input("Seleccione alguna comida que desee agregar al carrito: ")
            for elemento in lista_menu:
                if item in elemento.values():
                    carrito_user.append(elemento)
        if opcion == "n":
            break

def buscar_ingrediente(lista_carrito,ingrediente):
    for comida in lista_carrito:
        ing = comida["ingredientes"]
        if ingrediente in ing:
            print(comida)










