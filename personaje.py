from abc import ABC
from habilidades import Habilidades

class Personaje(Habilidades, ABC):
    def __init__(self, nombre="", hp=100, daño=0):
        self.nombre = nombre           
        self._nivel = 1                
        self.__hp = hp                 
        self.__daño = daño            
        self._cooldown = 2             

    def recibir_daño(self, daño):
        self.__hp -= daño
        if self.__hp < 0:
            self.__hp = 0

    def ver_hp(self):
        return self.__hp

    def subir_nivel(self):
        self._nivel += 1
        self.__daño += 1
        self.__hp = 100
        print(f"{self.nombre} ha subido a nivel {self._nivel}")
        print(f"El daño ahora es {self.__daño}")
        print(f"HP restaurado a {self.__hp}%")
