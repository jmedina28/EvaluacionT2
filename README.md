 <h1 align="center">Evaluación Tema 2</h1>

<h3 align="center">Perfil de GitHub del autor de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)

---
En este [repositorio](https://github.com/jmedina28/EvaluacionT2) queda completada la evaluación del tema 2.
***

El ejercicio 1 queda resuelto con este código:

```python

class Alumno:
    def __init__(self, nombre, apellido, nota):
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota
        print(f"El alumno: {self.nombre} {self.apellido} se ha creado con éxito.")
    
    def calificacion(self):
        if self.nota >= 5:
            return "Aprobado"
        else:
            return "Suspenso"
```

El ejercicio 2 queda resuelto con este código:

```python

class Alumno:
    def __init__(self, nombre, apellido, nota):
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota
        
    def __str__(self):
        return f"El alumno: {self.nombre} {self.apellido} con una nota de {self.nota} se ha creado con éxito." 
    
    def calificacion(self):
        if self.nota >= 5:
            return "Aprobado"
        else:
            return "Suspenso"

alumno1 = Alumno("Juan", "Pérez", 7)
alumno2 = Alumno("Maria", "García", 4)

print(alumno1)
print(alumno2)

print(alumno1.calificacion())
print(alumno2.calificacion())

```

El ejercicio 3 queda resuelto con este código:

```python
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
```

El ejercicio 4 queda resuelto con este código:

```python

try:
    resultado = 7/0
except ZeroDivisionError:
    print("Error: No es posible dividir entre cero, introduzca un número distinto.")

lista = [4, 7, 30, 23, 5]

try:
    lista[10]
except IndexError:
    print("Error: El índice al que intenta usted acceder se encuentra fuera del rango que abarca la lista, introduzca un número mayor o igual que cero y menor que la longitud de la lista.")

paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 

try:
    paises["alemania"]
except KeyError:
    print("Error: El país al que intenta usted acceder no se encuentra en el diccionario, introduzca un país que se encuentre en el diccionario.")

try:
    resultado = "2" + 10
except TypeError:
    print("Error: No es posible sumar un número y una cadena de texto, introduzca un número o una cadena de texto.")
```

El ejercicio 5 queda resuelto con este código:

```python
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

def catalogar(vehiculos, ruedas = None):
      
    if ruedas != None:
        cuenta = 0
        for vehiculo in vehiculos:
            if vehiculo.ruedas == ruedas: 
                cuenta += 1
        print("\nSe han encontrado {} vehículos con {} ruedas:".format(cuenta, ruedas))
    
    for vehiculo in vehiculos:
        if ruedas == None:
            print(type(vehiculo).__name__, vehiculo)
        else:
            if vehiculo.ruedas == ruedas:
                print(type(vehiculo).__name__, vehiculo)

catalogar(vehiculos,4)
```
