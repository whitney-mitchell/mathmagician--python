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
# Step 1 - Write your unit tests to reflect what classes, methods, and I/O is expected for each feature.

# Step 2 - Your program will have one class with a minimum of three methods on it:
# print_integers(self)
# print_fibonacci(self)
# print_primes(self)
# Each method should also accept an argument that determines how many numbers should be in the output.

# Write unit tests that will verify the output of each method.
# Do not write any implementation code until you have a unit test for each method that fails.

# Step 3 - Build menu first. Mkae last option "4. Quit program".
# When the user selects that option, make sure the program terminates.

# Create a simple implementation of a console application that displays a
# prompt to the user, and listens for a key press.
# Use print() to output the message Press any key to exit.
# Use input to accept user input, so that when your program runs, you press a key and it exits.

# Step 4 - Now you'll write the implementation code for your three methods,
# and the operation of the program itself.

# 1. You want it to do one of three mathematical operations.
# Update your prompt to be I am the Math Magician. What would you like me to do?
# The options will be Fibonacci, Primes, or Integers.

# user_choice = input('I am the Math Magician. What would you like me to do? ')

# 2. The goal here is that once the user tells the program what operation to perform,
# it will spit out the numbers forever until you “ctrl+c”.
# print(“Ok. I’m going to help produce " + user_choice);
# 3. Use time.sleep(seconds) when you output each number to the console to make each
# number legible (otherwise it goes too fast).
# 4. Make sure that your code validates user input. As a software developer, part of your job
# will be to handle edge cases. Think about possible things that the user can do that don't match what you expect of them, because they will. For example, at the prompt, they could type in the string Integers.

# Step 5 - Document your implementation code with docstrings.

# To test if magic works/runs, set a limit. Use a loop.
