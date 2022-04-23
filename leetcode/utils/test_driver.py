import unittest
from driver import Driver


class DriverTestCases(unittest.TestCase):

    def test_load_solution(self):
        def my_function(num1, num2):
            return num1 + num2
        
        input = {
            "num1": 1,
            "num2": 2
        }
        output = 3

        self.assertEqual(Driver.load_solution(my_function, input), output)
    
    def test_run_test_cases(self):
        pass


if __name__ == '__main__':
    unittest.main()
