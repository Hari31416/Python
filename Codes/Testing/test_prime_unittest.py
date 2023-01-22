import unittest
from prime import is_prime
from unittest import TestCase


class TestPrime(TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(99990001))
        self.assertFalse(is_prime(99990002))


if __name__ == "__main__":
    unittest.main()
