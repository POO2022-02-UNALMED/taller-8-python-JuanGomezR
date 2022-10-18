from ast import Str
from persona import Persona
from deportista import Deportista

class Futbolista(Persona,Deportista):
    listaFutbolistas=[]
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self,nombre, edad, altura, sexo)
        Deportista.__init__(self,"Futbol",añosPracticando)
        self.golesMarcados=golesMarcados
        self.tarjetasRojas=tarjetasRojas
        self.piernaHabil=piernaHabil
        Futbolista.listaFutbolistas.append(self)
    def __str__(self):
        return "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(self.nombre, self.deporte, self.edad, self.añosPracticando)
    def getGolesMarcados(self):
        return self.golesMarcados
    def getTarjetasRojas(self):
        return self.tarjetasRojas
    def getPiernaHabil(self):
        return self.piernaHabil
    def setGolesMarcados(self,golesMarcados):
        self.golesMarcados=golesMarcados
    def setTarjetasRojas(self,tarjetasRojas):
        self.tarjetasRojas=tarjetasRojas
    def setPiernaHabil(self,piernaHabil):
        self.piernaHabil=piernaHabil