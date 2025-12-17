import personaje
class Compi(personaje):
    def __init__(self, compi, nivel, clase ):
        super().__init__(clase, nivel)
        self.compi = compi

    @property
    def nivel(self):
        return super().__init__(self._nivel)
        
    nivel.setter
    def nivel(self, nuevo_nivel):
        self._nivel = nuevo_nivel