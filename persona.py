class Persona():
    def __init__(self, nombre, edad, altura):
        self.nombre=nombre
        self.edad=edad
        self.altura=altura
    
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getAltura(self):
        return self.altura
    def setNombre(self,nombre):
        self.nombre=nombre
    def setEdad(self,edad):
        self.edad=edad
    def setAltura(self,altura):
        self.altura=altura