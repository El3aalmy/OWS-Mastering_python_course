# ---------------------------------------------------
# -- Advanced lessons => Unit testing with unittes --
# ---------------------------------------------------
# Test runner 
# - The module that run unit testing (unittest, pytest)
# ---------------------------------------------------
# Test case 
# - Smallest unit of testing 
# - It use asserts methods to chek for actions and resposes 
# test suite 
# - Collection of multiple tests or test cases 
# Test report 
# - A full report contains the failure or succeed
# ---------------------------------------------------
# unittest
# - Add tests into classas ans methods
# - Use a series of special assertion methods 
# https://docs.python.org/3/library/unittest.html
# ---------------------------------------------------

import unittest

# assert 3 * 8 == 24, "Shoud be 24" # No error
# assert 3 * 8 == 25, "Shoud be 24" # Error

# def test_case_one():

#     assert 5 * 10 == 50, "Should be 50"

# def test_case_two():

#     assert 5 * 50 == 240, "Should be 250"

# if __name__ == "__main__":

#     test_case_one()
#     test_case_two()

#     print("All tests passed")   # Costum report 


class MyTestCase(unittest.TestCase):

    def test_one(self):

        self.assertTrue(100 > 99, "Should be true")

    def test_two(self):

        self.assertEqual(40 + 60, 100, "Should be 100")

    def test_three(self):

        self.assertGreater(100, 101, "Should be true")

if __name__ == "__main__":

    unittest.main()

