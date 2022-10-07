from introducir import solicitar_introducir_numero
from introducir.numero import solicitar_introducir_numero_extremo


seleccion = solicitar_introducir_numero_extremo("Introduzca el número del ejercicio que desea ejecutar: ", 1, 5)

if seleccion == 1:
    from ejercicios.ejercicio1 import Alumno
    alumno = Alumno("Juan", "Pérez", 7)
    print(alumno.calificacion())
    alumno2 = Alumno("Maria", "García", 4)
    print(alumno2.calificacion())

elif seleccion == 2:
    from ejercicios.ejercicio2 import Alumno
    alumno = Alumno("Juan", "Pérez", 7)
    print(alumno)
    print(alumno.calificacion())
    alumno2 = Alumno("Maria", "García", 4)
    print(alumno2)
    print(alumno2.calificacion())
    
elif seleccion == 3:
    from ejercicios.ejercicio3 import Producto

    producto = Producto("0001","Producto 1","Descripción del producto 1",100)
    print(producto)
    producto.pvp = 200
    print(""),print(producto)

elif seleccion == 4:
    import ejercicios.ejercicio4

elif seleccion == 5:
    from ejercicios import ejercicio5
