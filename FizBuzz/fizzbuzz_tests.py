import unittest
import FizBuzz

class TestCase(unittest.TestCase):
    def testFizz(self):
        result = FizBuzz.is_fizz(20)
        self.assert(result, False)

        result = FizBuzz.is_fizz(21)
        self.assert(result, True)
        
