import unittest
from Fizz_Buzz import fizz_buzz_jit, measure_time, compare


class TestFizzBuzz (unittest.TestCase):
    def setUp(self):
        self.fizz_buzz = fizz_buzz_jit

    def test_returns_fizz_for_multiples_of_three(self):
        self.assertEqual (self.fizz_buzz (3), 'Fizz')
        self.assertEqual (self.fizz_buzz (6), 'Fizz')

    def test_returns_buzz_for_multiples_of_five(self):
        self.assertEqual (self.fizz_buzz (5), 'Buzz')
        self.assertEqual (self.fizz_buzz (10), 'Buzz')

    def test_returns_fizzbuzz_for_multiples_of_fifteen(self):
        self.assertEqual (self.fizz_buzz (15), 'FizzBuzz')
        self.assertEqual (self.fizz_buzz (30), 'FizzBuzz')

    def test_returns_number_for_other_numbers(self):
        self.assertEqual (self.fizz_buzz (1), '1')
        self.assertEqual (self.fizz_buzz (2), '2')
        self.assertEqual (self.fizz_buzz (4), '4')

    def test_measure_time_returns_positive_number(self):
        time_taken = measure_time (self.fizz_buzz, 100)
        self.assertGreaterEqual (time_taken, 0)  # change assertion

    def test_compare_does_not_raise_exception(self):
        try:
            compare ()
        except Exception as e:
            self.fail (f"compare() raised {type (e)} unexpectedly!")


if __name__ == '__main__':
    unittest.main ()
