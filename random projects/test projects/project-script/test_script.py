# import unittest
# import script

# class TestScript(unittest.TestCase):
#     def setUp(self):
#         print('start of the test')


#     def test_add(self):
#         test_arg = 10
#         result = script.add(test_arg)
#         self.assertEqual(result, 15)


#     def test_add2(self):
#         test_arg = 'sldkfj'
#         result = script.add(test_arg)
#         self.assertIsInstance(result, ValueError)


#     def test_add3(self):
#         test_arg = None
#         result = script.add(test_arg)
#         self.assertEqual(result, 'please enter a number')


#     def test_add4(self):
#         test_arg = ''
#         result = script.add(test_arg)
#         self.assertEqual(result, 'please enter a number')


#     def test_add5(self):
#         test_arg = 0
#         result = script.add(test_arg)
#         self.assertEqual(result, 'please enter a number')


#     def tearDown(self):
#         print('the end')


# if __name__ == '__main__':
#     unittest.main()
