import unittest
import app as app
from datetime import datetime

class TestArithmeticProgression(unittest.TestCase):
    
    def setUp(self):     # basic setup
        self.prog = app
    

    # first command
    def test_arithmetic_progression_sum(self):
        self.assertEqual(app.arithmetic_progression(0), 0)    # comparing values (input with result)
        self.assertEqual(app.arithmetic_progression(1), 2)
        self.assertEqual(app.arithmetic_progression(2), 6)
        self.assertEqual(app.arithmetic_progression(4), 20)
        self.assertEqual(app.arithmetic_progression(11), 132)

    def test_arith_sum_exception(self):
        with self.assertRaises(Exception):
            app.arithmetic_progression(-1)   # returns true = exception occurs


    # second command
    def test_geometric_progression_sum(self):
        self.assertEqual(app.geometric_progression(0), 0)   # comparing values (input with result)
        self.assertEqual(app.geometric_progression(1), 2)
        self.assertEqual(app.geometric_progression(2), 3)
        self.assertEqual(app.geometric_progression(3), 3.5)
        self.assertEqual(app.geometric_progression(4), 3.75)

    def test_geometric_sum_exception(self):
        with self.assertRaises(Exception):
            app.geometric_progression(-10)   # returns true = exception occurs


    # third command
    def test_days_til_birthday_next_year(self):  # birthday another year
        birthdate = datetime(2024, 6, 1)
        today = datetime(2023, 12, 19)
        self.assertEqual(app.days_til_birthday(birthdate, today), 165)  
    
    def test_days_til_birthday_today(self):  # birthday today
        birthdate = datetime(2023, 12, 19)
        today = datetime(2023, 12, 19)
        self.assertEqual(app.days_til_birthday(birthdate, today), 0)   
    
    def test_days_til_birthday_this_year(self):  # birthday this year
        birthdate = datetime(2023, 12, 19)
        today = datetime(2023, 1, 19)
        self.assertEqual(app.days_til_birthday(birthdate, today), 334)

    def test_days_til_birthday_that_has_been(self):  # birthday that has already passed, one year mus be added
        birthdate = datetime(2023, 2, 19)
        today = datetime(2023, 12, 19)
        self.assertEqual(app.days_til_birthday(birthdate, today), 62)


    def tearDown(self):    # tear down
        pass

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()