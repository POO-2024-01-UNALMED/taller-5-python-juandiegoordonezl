from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas=0
    salamandras=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self.venenoso=venenoso
        Anfibio._listado.append(self)
     
    @classmethod 
    def cantidadAnfibios(cls):
        return (len(Anfibio._listado))
    
    @classmethod
    def movimiento(cls):
        return "saltar"
    
    @staticmethod
    def crearRana(cls,nombre,edad,genero):
        rana=Anfibio(nombre,edad,"selva",genero,"rojo",True)
        cls.ranas+=1
        return rana
    
    @staticmethod
    def crearSalamandra(cls,nombre,edad,genero):
        salamandra=Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        cls.salamandras+=1
        return salamandra
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self,colorPiel):
        self._colorPiel=colorPiel
    
    def isVenenoso(self):
        return self._venenoso
    
    def isVenenoso(self,venenoso):
        self._venenoso=venenoso