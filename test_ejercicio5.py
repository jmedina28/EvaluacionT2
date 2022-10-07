import unittest
from ejercicios.ejer5.ejercicio5 import Vehiculo, Coche, Camioneta, Bicicleta, Motocicleta

class TestEjercicio5(unittest.TestCase):
    
        def test_vehiculo(self):
            vehiculo = Vehiculo("rojo", 4)
            self.assertEqual(vehiculo.color, "rojo")
            self.assertEqual(vehiculo.ruedas, 4)
            self.assertEqual(str(vehiculo), "color rojo, 4 ruedas")
    
        def test_coche(self):
            coche = Coche("azul", 4, 150, 1300)
            self.assertEqual(coche.color, "azul")
            self.assertEqual(coche.ruedas, 4)
            self.assertEqual(coche.velocidad, 150)
            self.assertEqual(coche.cilindrada, 1300)
            self.assertEqual(str(coche), "color azul, 4 ruedas, 150 km/h, 1300 cc")
    
        def test_camioneta(self):
            camioneta = Camioneta("verde", 4, 90, 2000, 750)
            self.assertEqual(camioneta.color, "verde")
            self.assertEqual(camioneta.ruedas, 4)
            self.assertEqual(camioneta.velocidad, 90)
            self.assertEqual(camioneta.cilindrada, 2000)
            self.assertEqual(camioneta.carga, 750)
            self.assertEqual(str(camioneta), "color verde, 4 ruedas, 90 km/h, 2000 cc, soporta 750 kg de carga")
    
        def test_bicicleta(self):
            bici1 = Bicicleta("rosa", 2, "urbana")
            self.assertEqual(bici1.color, "rosa")
            self.assertEqual(bici1.ruedas, 2)
            self.assertEqual(bici1.tipo, "urbana")
            self.assertEqual(str(bici1), "color rosa, 2 ruedas, urbana")
    
        def test_motocicleta(self):
            moto1 = Motocicleta("negra", 2, "deportiva", 200, 600)
            self.assertEqual(moto1.color, "negra")
            self.assertEqual(moto1.ruedas, 2)
            self.assertEqual(moto1.tipo, "deportiva")
            self.assertEqual(moto1.velocidad, 200)
            self.assertEqual(moto1.cilindrada, 600)
            self.assertEqual(str(moto1), "color negra, 2 ruedas, deportiva, 200 km/h, 600 cc")
        

if __name__ == '__main__':
    unittest.main()