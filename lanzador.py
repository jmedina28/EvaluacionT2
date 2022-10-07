from introducir.numero import solicitar_introducir_numero_extremo


def ejecutar():
    
    seleccion = solicitar_introducir_numero_extremo("Introduzca el número del ejercicio que desea ejecutar: ", 1, 5)
    if seleccion == 1:
        from ejercicios.ejer1.ejercicio1 import Alumno
        alumno = Alumno("Juan", "Pérez", 7)
        print(alumno.calificacion())
        alumno2 = Alumno("Maria", "García", 4)
        print(alumno2.calificacion())

    elif seleccion == 2:
        from ejercicios.ejer2.ejercicio2 import Alumno
        alumno = Alumno("Juan", "Pérez", 7)
        print(alumno)
        print(alumno.calificacion())
        alumno2 = Alumno("Maria", "García", 4)
        print(alumno2)
        print(alumno2.calificacion())

    elif seleccion == 3:
        from ejercicios.ejer3.ejercicio3 import Producto

        producto = Producto("0001","Producto 1","Descripción del producto 1",100)
        print(producto)
        producto.pvp = 200
        print("El nuevo PVP es: ", producto.pvp)
        print(""),print(producto)

    elif seleccion == 4:
        import ejercicios.ejer4.ejercicio4

    elif seleccion == 5:
        import ejercicios.ejer5.ejercicio5