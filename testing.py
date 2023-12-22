import unittest
import app as app

class TestArithmeticProgression(unittest.TestCase):
    
    def setUp(self):     # basic setup
        self.prog = app
    

    # first command
    def test_arithmetic_progression_sum(self):
        self.assertEqual(app.arithmetic_progression(0), 0)    # comparing values (input with result)
        self.assertEqual(app.arithmetic_progression(1), 1)
        self.assertEqual(app.arithmetic_progression(2), 6)
        self.assertEqual(app.arithmetic_progression(3), 15)
        self.assertEqual(app.arithmetic_progression(4), 28)
        self.assertEqual(app.arithmetic_progression(11), 231)

    def test_arith_sum_exception(self):
        with self.assertRaises(Exception):
            app.arithmetic_progression(-1)   # returns true = exception occurs


    def tearDown(self):    # tear down
        pass

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()