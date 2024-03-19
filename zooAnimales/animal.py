import zooAnimales
from gestion.zona import Zona
class Animal:
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=None
        Animal._totalAnimales += 1
    def movimiento(self):
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        return "Mamiferos : " + str(zooAnimales.mamifero.Mamifero.cantidadMamiferos()) + "\nAves : " + str(zooAnimales.ave.Ave.cantidadAves()) + "\nReptiles : " + str(zooAnimales.reptil.Reptil.cantidadReptiles()) + "\nPeces : " + str(zooAnimales.pez.Pez.cantidadPeces()) + "\nAnfibios : " + str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre=nombre
    
    def getEdad(self):
        return self._edad
    
    def setEdad(self,edad):
        self._edad=edad
        
    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self,habitat):
        self._habitat=habitat
        
    def getGenero(self):
        return self._genero
    
    def setGenero(self,genero):
        self._genero=genero
        
    def getZona(self):
        return self._zona
    
    def setZona(self,zona):
        self._zona=zona
    
    def toString(self):
        if self._zona!=[]:
            return "Mi nombre es "+self._nombre+", tengo una edad de "+str(self._edad)+", habito en "+self.habitat+" y mi genero es "+self._genero+", la zona en la que me ubico es "+self._zona[0].getNombre()+", en el "+self._zona[0].getZoo().getNombre()
        else:
            return "Mi nombre es "+self._nombre+", tengo una edad de "+str(self._edad)+", habito en "+self.habitat+" y mi genero es "+self._genero