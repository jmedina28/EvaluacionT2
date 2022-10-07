import unittest
from ejercicios.ejer1.ejercicio1 import Alumno
class TestEjercicio1(unittest.TestCase):

    def test_alumno(self):
        alumno1 = Alumno("Juan", "Pérez", 7)
        alumno2 = Alumno("Maria", "García", 4)
        self.assertEqual(alumno1.calificacion(), "Aprobado")
        self.assertEqual(alumno2.calificacion(), "Suspenso")

if __name__ == '__main__':
    unittest.main()