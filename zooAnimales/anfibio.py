from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas=0
    salamandras=0
    listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)

        self._colorPiel=colorPiel
        self.venenoso=venenoso
        Anfibio.agregarListado(self)
    
    @classmethod     
    def agregarListado(cls,a):
        cls.listado.append(a)
    
    @classmethod 
    def cantidadAnfibios(cls):
        return (len(cls.listado))
    
    @staticmethod
    def crearRana(cls,nombre,edad,genero):
        rana=Anfibio(nombre,edad,"selva",genero,"rojo",True)
        cls.ranas+=1
        Anfibio.agregarlistado(rana)
        return rana
    
    @staticmethod
    def crearSalamandra(cls,nombre,edad,genero):
        salamandra=Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        cls.salamandras+=1
        Anfibio.agregarlistado(salamandra)
        return salamandra
    
    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self,colorPiel):
        self._colorPiel=colorPiel
    
    def getVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self,venenoso):
        self._venenoso=venenoso