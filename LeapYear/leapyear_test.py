import unittest
import leapyear

class LeapYearTest(unittest.TestCase):
    def test_is_leap_year(self):
        result = leapyear.is_leap_year(400)
        self.assertEqual(result, True)

        result = leapyear.is_leap_year(100)
        self.assertFalse(result)

        result = leapyear.is_leap_year(4)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
