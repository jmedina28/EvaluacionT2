import unittest
from ejercicios.ejercicio3 import Producto

class TestEjercicio3(unittest.TestCase):
    
        def test_producto(self):
            producto1 = Producto("0001","Producto 1","Descripción del producto 1",100)
            producto2 = Producto("0002","Producto 2","Descripción del producto 2",200)
            self.assertEqual(producto1.pvp, 100)
            self.assertEqual(producto2.pvp, 200)
            producto1.pvp = 300
            self.assertEqual(producto1.pvp, 300)


if __name__ == '__main__':
    unittest.main()