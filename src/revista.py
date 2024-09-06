class Revista(Publicación):
    def __init__(self, titulo, ano_publicacion, numero_revista, nombre_revista):
        super().__init__(titulo, ano_publicacion)
        self._numero_revista = numero_revista
        self._nombre_revista = nombre_revista

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de la revista: {self._numero_revista}")
        print(f"Nombre de la revista: {self._nombre_revista}")

    def numero_revista(self):
        return self._numero_revista

    def numero_revista(self, valor):
        self._numero_revista = valor
 
    def nombre_revista(self):
        return self._nombre_revista

    def nombre_revista(self, valor):
        self._nombre_revista = valor
    
