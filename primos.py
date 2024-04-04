import unittest

def is_primo(value):
    
    if value == 2:
        return  True
    for n in range(2, value):
       
        if value % n == 0:
            return False
    return True

class testPrimo (unittest.TestCase):
    def test1(self):
        result =is_primo(1)
        self.assertEqual(result, True)
    def test2(self):
        result =is_primo(2)
        self.assertEqual(result, True)
    def test3(self):
        result =is_primo(3)
        self.assertEqual(result, True)
    def test4(self):
        result =is_primo(4)
        self.assertEqual(result, False)
    def test5(self):
        result =is_primo(5)
        self.assertEqual(result, True)
    def test14(self):
        result =is_primo(14)
        self.assertEqual(result, False)
    def test11(self):
        result =is_primo(11)
        self.assertEqual(result, True)
    def test9(self):
        result =is_primo(9)
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()   