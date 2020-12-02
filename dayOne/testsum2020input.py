import unittest

# target = __import__("sum2020input.py")
import dayOne

class TestSum(unittest.TestCase):
    def test_find_two_values(self):
        """
        Test that it can find two values
        """
        set = {2020, 0}
        result = find_two_values(set)
        self.assertEqual(result[0], 2020)

if __name__ == '__main__':
    unittest.main()
