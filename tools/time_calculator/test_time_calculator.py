import unittest
from time_calculator import add_two_times

class TimeCalculatorTestCase(unittest.TestCase):
    
    def test_add_two_times(self):
        self.assertEqual(add_two_times("1.30", "1.30"), "3.0")
        self.assertEqual(add_two_times("1.10", "1.50"), "3.0")
        self.assertEqual(add_two_times("1.30", "1.50"), "3.20")
        self.assertEqual(add_two_times("1.50", "1.50"), "3.40")
        self.assertEqual(add_two_times("1.10", "1.25"), "2.35")
        
if __name__ == '__main__':
    unittest.main()