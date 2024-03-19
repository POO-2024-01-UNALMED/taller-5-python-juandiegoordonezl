from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas=0
    serpientes=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._listado.append(self)
       

    @classmethod
    def cantidadReptil(cls):
        return (len(Reptil._listado))
    
    @classmethod
    def movimiento(cls):
        return "reptar"
   

    @staticmethod
    def crearIguana(cls,nombre,edad,genero):
        iguana=Reptil(nombre,edad,"humedal",genero,"verde",3)
        cls.iguanas+=1
        return iguana
    @staticmethod
    def crearSerpiente(cls,nombre,edad,genero):
        serpiente=Reptil(nombre,edad,"jungla",genero,"blanco",1)
        cls.serpientes+=1
        return serpiente
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas=colorEscamas
    
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self,largoCola):
        self._largoCola=largoCola