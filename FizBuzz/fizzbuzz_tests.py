import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def testFizz(self):
        result = fizzbuzz.is_fizz(20)
        self.assertFalse(result)

        result = fizzbuzz.is_fizz(21)
        self.assertTrue(result)

    def testBuzz(self):
        self.assertFalse(fizzbuzz.is_buzz(2))

        self.assertTrue(fizzbuzz.is_buzz(5))

    def testFizzBuzz(self):
        result = fizzbuzz.fizzbuzz(1)
        self.assertEqual(result, 1)

        result = fizzbuzz(3)
        self.assertEqual(result, 'Fizz')

        result = fizzbuzz(5)
        self.assertEqual(result, 'Buzz')

        result = fizzbuzz(15)
        self.assertEqual(result, 'FizzBuzz')
        
if __name__ == '__main__':
    unittest.main()
