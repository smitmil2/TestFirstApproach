import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def testFizz(self):
        result = fizzbuzz.is_fizz(20)
        self.assertFalse(result)

        result = fizzbuzz.is_fizz(21)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
