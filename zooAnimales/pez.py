from zooAnimales.animal import Animal

class Pez(Animal):
    salmones=0
    bacalaos=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=cantidadAletas
        Pez._listado.append(self)

    @classmethod
    def cantidadPeces(cls):
        return (len(Pez._listado))
    
    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        salmon=Pez(nombre,edad,"oceano",genero,"rojo",6)
        cls.salmones+=1
        return salmon
    
    @classmethod
    def movimiento(cls):
        return "nadar"
    
    
    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        bacalao=Pez(nombre,edad,"oceano",genero,"gris",6)
        cls.bacalaos+=1
        return bacalao
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self,colorEscamas):
        self._colorEscamas=colorEscamas
    
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self,cantidadAletas):
        self._cantidadAletas=cantidadAletas