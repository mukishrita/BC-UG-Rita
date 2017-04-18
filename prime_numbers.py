import unittest
from prime import generate_prime

class PrimeNumberTestCases(unittest.TestCase):

    def test_for_correct_answer_including_number(self):
        result = generate_prime(11)
        self.assertEqual(result, [1,2,3,5,7,11] , msg='Wrong answers')

    def test_for_another_right_answer_without_number(self):
        result = generate_prime(20)
        self.assertEqual(result, [1,2,3,5,7,11,13,17,19] , msg='Wrong answers')

    def test_only_list_returned(self):
        result = generate_prime(9)
        self.assertEqual(type(result), list , msg='Invalid output')

    def test_for_not_allowing_non_integer(self):
        with self.assertRaises(ValueError) as context:
            generate_prime('string')
            self.assertEqual(
                "The provided input is not an integer.",
                context.exception.message, "Invalid input not allowed"
            )

    def test_to_check_that_all_items_in_list_are_integers(self):
        result = generate_prime(20)
        self.assertTrue(all(isinstance(n, int) for n in result), msg="Some of the items in the list are not integers")

    def test_for_negative_values(self):
        result = generate_prime(-3)
        self.assertEqual(result, [], msg='It should return an empty list for negative times.')

    def test_for_when_no_variable_is_passed(self):
        with self.assertRaises(ValueError) as context:
            generate_prime()
            self.assertEqual(
                "The provided input is not an integer.",
                context.exception.message, "Invalid input not allowed"
            )

if __name__ == '__main__' : unittest.main()
class PrimeNumberTestCases(unittest.TestCase):
