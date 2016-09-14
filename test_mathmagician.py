import unittest
from mathmagician import *

class Test_mathmagician(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.magician = Mathmagician()

	def test_print_integers_returns_correct_integers(self):
		integers = self.magician.generate_integers(8)
		self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7], integers)


	def test_print_fibonacci_returns_correct_sequence(self):
		fib_digits = self.magician.generate_fibonacci(6)
		self.assertEqual([0, 1, 1, 2, 3, 5], fib_digits)


	def test_print_primes_returns_correct_sequence(self):
		primes = self.magician.generate_primes(4)
		self.assertEqual([2, 3, 5, 7], primes)



if __name__ == '__main__':
    unittest.main()

