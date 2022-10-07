class Producto:
    def __init__(self,referencia,nombre,descripcion,pvp):
        self.referencia = referencia
        self.nombre = nombre
        self.descripcion = descripcion
        self.pvp = pvp
        
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
DESCRIPCIÓN\t{}
PVP\t\t{}""".format(self.referencia,self.nombre,self.descripcion,self.pvp)

producto = Producto("0001","Producto 1","Descripción del producto 1",100)
print(producto)