import unittest
from process_list import process_list

class TestProcessListFunction(unittest.TestCase):
    def test_valid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        processed_result = process_list(input_list)
        self.assertEqual(processed_result, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

    def test_invalid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        with self.assertRaises(ValueError):
            process_list(input_list)

if __name__ == "__main__":
    unittest.main()
