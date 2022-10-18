from persona import Persona
from deportista import Deportista

class Futbolista(Persona,Deportista):
    listaFutbolistas=[]
    def __init__(self, nombre, edad, altura, deporte, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(nombre, edad, altura)
        Deportista.__init__(deporte,añosPracticando)
        self.golesMarcados=golesMarcados
        self.tarjetasRojas=tarjetasRojas
        self.piernaHabil=piernaHabil
        Futbolista.listaFutbolistas.append(self)
    def __str__(self):
        return ("mi nombre es ",self.nombre," soy profesional en el deporte ", self.deporte, " Tengo ",self.edad,
        " años de edad y llevo ", self.añosPracticando, " años en el deporte")
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