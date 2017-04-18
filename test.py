import unittest

class TestPrimeNumberGenerator(unittest.TestCase):

    def test_int(self):
        self.assertIsNot(generate_prime_numbers("stuff"),"range is not integer")

    def test_not_negative(self):
        self.assertIsNot(generate_prime_numbers(-1),"range is a negative number")

    def test_prime_numbers(self):
        self.assertEqual(generate_prime_numbers(10),[2,3,5,7])


def generate_prime_numbers(n):
    prime_numbers = []
    test_numbers = [2,3]
    if isinstance(n, int):
        if n > 0:
            for num in range(2, n):
                if num in test_numbers:
                    prime_numbers.append(num)
                else:
                    is_prime = True
                    for test_number in test_numbers:
                        if num % test_number == 0:
                            is_prime = False
                    if is_prime == True:
                        prime_numbers.append(num)
            return prime_numbers
        else:
            return "range is a negative number"
    else:
        return "range is not integer"

if __name__ == '__ma