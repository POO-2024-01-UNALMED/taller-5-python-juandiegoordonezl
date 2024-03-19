from zooAnimales.animal import Animal

class Mamifero(Animal):
    caballos=0
    leones=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)
   
    @classmethod
    def cantidadMamiferos(cls):
        return (len(Mamifero._listado))
    
    @staticmethod
    def crearCaballo(cls,nombre,edad,genero):
        caballo=Mamifero(nombre,edad,"pradera",genero,True,4)
        cls.caballos+=1
        return caballo
    @staticmethod
    def crearLeon(cls,nombre,edad,genero):
        leon=Mamifero(nombre,edad,"selva",genero,True,4)
        cls.leones+=1
        return leon
    
    def isPelaje(self):
        return self._pelaje
    
    def isPelaje(self,pelaje):
        self._pelaje=pelaje
        
    def getPatas(self):
        return self._patas
    
    def setPatas(self,patas):
        self._patas=patas