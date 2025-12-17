
import personaje
class Personaje:
    def __init__(self, nombre, nivel, clase ):
        self.nombre = nombre
        self._nivel = nivel
        self.__clase = clase

    @property
    def nivel(self):
        return self._nivel
        
    nivel.setter
    def nivel(self, nuevo_nivel):
        self._nivel = nuevo_nivel