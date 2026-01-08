from abc import ABC
from habilidades import Habilidades

class Enemigo(Habilidades, ABC):
    def __init__(self, nombre="Enemigo", hp=80, daño=12):
        self.nombre = nombre           
        self._nivel = 1                
        self.__hp = hp                 
        self.__daño = daño             
        self._cooldown = 2             

    def atacar(self, objetivo):
        if self._cooldown >= 2:
            self.usar_habilidad(objetivo)
            self._cooldown = 0
        else:
            self._cooldown += 1
            objetivo.recibir_daño(self.__daño)
            print(f"{self.nombre} ataca y hace {self.__daño} de daño")

    def recibir_daño(self, daño):
        self.__hp -= daño
        if self.__hp < 0:
            self.__hp = 0

    def ver_hp(self):
        return self.__hp
