class Libro(Publicación):
     def __init__(self, titulo, ano_publicacion, autor, numero_paginas):
        super().__init__(titulo, ano_publicacion)
        self._autor = autor
        self._numero_paginas = numero_paginas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Autor: {self._autor}")
        print(f"Número de páginas: {self._numero_paginas}")

    def autor(self):
        return self._autor

    def autor(self, valor):
        self._autor = valor

    def numero_paginas(self):
        return self._numero_paginas

    def numero_paginas(self, valor):
        self._numero_paginas = valor
    
