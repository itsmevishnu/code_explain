import unittest
from collections import Counter


def find_counts(input_list: list) -> dict:

    if len(input_list) == 0:
        return {}
    
    counter = Counter(input_list)
    
    return dict(counter)

class TestFindCounts(unittest.TestCase):

    def test_boundary_condition(self):
        actual_output = find_counts([])
        self.assertEqual(actual_output, {})
    
    def test_counter(self):
        input_list = [1,1,2]
        actual_output = find_counts(input_list=input_list)
        expected_output = {1:2, 2:1}
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()
