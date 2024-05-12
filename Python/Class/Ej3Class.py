class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"El libre se llama {self.titulo}, del autor {self.autor} y tiene {self.paginas} páginas"
    
libro_1 = Libro ("Hábitos Atómicos", "Armando Esteban Quito" , 569)

print(libro_1)