import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.scores = [2, 4, 10, 2, 5]

    # Test latest score (the last thing in the list)
    def test_can_get_latest_score(self):
        expected_value = 5
        actual_value = latest(self.scores)
        self.assertEqual(expected_value, actual_value)

    # Test personal best (the highest score in the list)
    def test_can_get_personal_best(self):
        expected_value = 10
        actual_value = personal_best(self.scores)
        self.assertEqual(expected_value, actual_value)


    # Test top three from list of scores
    def test_can_get_top_three(self):
        expected = [10, 5, 4]
        actual_value = personal_top_three(self.scores)
        self.assertEqual(expected, actual_value)


    # Test ordered from highest tp lowest
    # def test_ordered_highest_to_lowest(self):
    #     expected = [10, 5 ,4, 2, 2]
    #     actual_value = order_highest_to_lowest(self.scores)
    #     self.assertEqual(expected, actual_value)


    # Test top three when there is a tie
    def test_can_get_top_3_when_tied(self):
        scores = [2, 4, 10, 2, 5, 5]
        expected = [10, 5, 5]
        actual_value = personal_top_three(scores)
        self.assertEqual(expected, actual_value)




    # Test top three when there are less than three
    def test_get_top_3_when_less_than_3(self):
        scores = [1, 2]
        expected = [2, 1]
        actual_value = personal_top_three(scores)
        self.assertEqual(expected, actual_value)


    # Test top three when there is only one
    
    def test_get_top_3_when_less_than_1(self):
        scores = [1]
        expected = [1]
        actual_value = personal_top_three(scores)
        self.assertEqual(expected, actual_value)