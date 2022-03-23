import unittest
import main

class TestMain(unittest.TestCase):

    def test_addition(self):
        test_param1 = 4
        test_param2 = 8
        result = main.addition(test_param1, test_param2)
        self.assertEqual(result, 12)


    def test_subtraction(self):
        test_param1 = 10
        test_param2 = 5
        result = main.subtraction(test_param1, test_param2)
        self.assertEqual(result, 5)


    def test_multiplicaton(self):
        test_param1 = 10
        test_param2 = 5
        result = main.multiplication(test_param1, test_param2)
        self.assertEqual(result, 50)


    def test_division(self):
        test_param1 = 18
        test_param2 = 2
        result = main.division(test_param1, test_param2)
        self.assertEqual(result, 9)


    def test_division2(self):
        test_param1 = 18
        test_param2 = 0
        result = main.division(test_param1, test_param2)
        self.assertTrue(isinstance(result, ZeroDivisionError))
        

    def test_division3(self):
        test_param1 = 18
        test_param2 = 'really'
        result = main.division(test_param1, test_param2)
        self.assertTrue(isinstance(result, TypeError))


unittest.main()
