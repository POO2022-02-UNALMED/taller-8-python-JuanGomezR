class Persona():
    def __init__(self, nombre, edad, altura, sexo):
        self.nombre=nombre
        self.edad=edad
        self.altura=altura
        self.sexo=sexo
    
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getAltura(self):
        return self.altura
    def getSexo(self):
        return self.sexo
    def setNombre(self,nombre):
        self.nombre=nombre
    def setEdad(self,edad):
        self.edad=edad
    def setAltura(self,altura):
        self.altura=altura
    def setSexo(self,sexo):
        self.sexo=sexo