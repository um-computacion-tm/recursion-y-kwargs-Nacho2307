import unittest
def fibonacci(n):
    if n == 0:
        print(0)
        return 0
    if n == 1:
        print(1)
        return 1
    resultado = fibonacci(n-1) + fibonacci(n-2)
    print(resultado)
    return resultado

class testFibonacci(unittest.TestCase):
    def test_0(self):
        resultado = fibonacci(0)
        self.assertEqual(resultado, 0)
    def test_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)
    def test_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)
    def test_3(self):
        resultado = fibonacci(3)
        self.assertEqual(resultado, 2)
    def test_4(self):
        resultado = fibonacci(4)
        self.assertEqual(resultado, 3)
    def test_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 5)
    def test_6(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado, 8)


unittest.main()