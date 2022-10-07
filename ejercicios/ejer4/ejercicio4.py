
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