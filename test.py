import unittest
from main import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(6), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(10), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(30), "FizzBuzz")

    def test_number(self):
        self.assertEqual(fizz_buzz(1), "1")
        self.assertEqual(fizz_buzz(7), "7")


if __name__ == "__main__":
    unittest.main()
