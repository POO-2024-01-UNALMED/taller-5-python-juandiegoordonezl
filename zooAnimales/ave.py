from zooAnimales.animal import Animal

class Ave(Animal):
    halcones=0
    aguilas=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)
         
    @classmethod 
    def cantidadAve(cls):
        return (len(Ave._listado))
    
    @classmethod
    def movimiento(cls):
        return "volar"
    
    @staticmethod
    def crearHalcon(cls,nombre,edad,genero):
        halcon=Ave(nombre,edad,"montanas",genero,"cafe glorioso")
        cls.halcones+=1
        return halcon
    
    @staticmethod
    def crearAguila(cls,nombre,edad,genero):
        aguila=Ave(nombre,edad,"montanas",genero,"blanco y amarillo")
        cls.aguilas+=1
        return aguila
    
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self,colorPlumas):
        self._colorPlumas=colorPlumas