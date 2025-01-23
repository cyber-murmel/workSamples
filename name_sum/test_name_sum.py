#imports
import re
import unittest # Import the unit test module for writting and running tests
from name_sum import calculate_sum

#unit tests
class TestGetValidName(unittest.TestCase): # Unit test class for get_valid_name function
    def test_valid_name(self): # Defines test case
        pattern = r'^[A-Za-z ]+$'
        self.assertIsNotNone(re.match(pattern,"Ivan")) # Tests that valid name pass
        self.assertIsNone(re.match(pattern,"Iv@n")) # Test that invalid name fails
        self.assertIsNone(re.match(pattern,"1v4n"))
        """This test checks if the input matches the pattern 
        (english letter characters and spaces only) """

class TestCalculateSum(unittest.TestCase):
    def test_single_letters(self):
        """Test that the calculation of single letters is correct."""
        self.assertEqual(calculate_sum("A"), 1)
        self.assertEqual(calculate_sum("B"), 2)
        self.assertEqual(calculate_sum("Z"), 26)

    def test_case_insensitivity(self):
        """Test that the calculation is case insensitive."""
        self.assertEqual(calculate_sum("Az"), 27)
        self.assertEqual(calculate_sum("aZ"), 27)

    def test_white_space(self):
        """Test that calculation ignores whitespace."""
        self.assertEqual(calculate_sum(" Test "), 64)
        self.assertEqual(calculate_sum("T est"), 64)
        self.assertEqual(calculate_sum("Te   st"), 64)

if __name__ == "__main__": # execute the tests when script is executed direclty
    unittest.main() # Run all tests and displays the result



