from introducir import solicitar_introducir_numero


seleccion = solicitar_introducir_numero("Introduzca un número: ")

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
    from ejercicios import ejercicio3

elif seleccion == 4:
    from ejercicios import ejercicio4

elif seleccion == 5:
    from ejercicios import ejercicio5
