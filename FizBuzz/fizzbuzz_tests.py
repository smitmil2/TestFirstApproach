import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def testFizz(self):
        result = fizzbuzz.is_fizz(20)
        self.assertEqual(result, False)

        result = fizzbuzz.is_fizz(21)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
