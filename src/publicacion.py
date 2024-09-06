class Publicacion:
     def __init__(self, titulo, ano_publicacion):
        self._titulo = titulo
        self._ano_publicacion = ano_publicacion

    def mostrar_info(self):
        print(f"Título: {self._titulo}")
        print(f"Año de Publicación: {self._ano_publicacion}")
 
    def titulo(self):
        return self._titulo

    def titulo(self, valor):
        self._titulo = valor
 
    def ano_publicacion(self):
        return self._ano_publicacion

    def ano_publicacion(self, valor):
        self._ano_publicacion = valor
    
