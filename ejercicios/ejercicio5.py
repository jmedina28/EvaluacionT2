class Vehiculo():
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )
        
        
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

coche = Coche("azul", 4, 150, 1300)


class Camioneta(Coche):
    
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
        
    def __str__(self):
        return super().__str__() + ", soporta {} kg de carga".format(self.carga)

camioneta = Camioneta("verde", 4, 90, 2000, 750)


class Bicicleta(Vehiculo):
    
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
        
    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)

bici1 = Bicicleta("rosa", 2, "urbana")


class Motocicleta(Bicicleta):
    
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada) 
    
moto1 = Motocicleta("negra", 2, "deportiva", 200, 600)


vehiculos = [coche, camioneta, bici1, moto1]

def catalogar(vehiculos):
    for vehiculo in vehiculos:
        print(type(vehiculo).__name__, vehiculo)

catalogar(vehiculos)