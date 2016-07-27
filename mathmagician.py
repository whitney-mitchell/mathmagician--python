import time
import math

class Mathmagician():
	"""This class is the interface between the user and the Mathmagician machine
		(the logic that displays the numbers).

	Methods:
		show_menu
		generate_integers
		generate_fibonacci
		generate_primes
	"""
	# def __init__(self):
	# 	# menu = self.show_menu()
	# 	pass

	def show_menu(self):
		print("Type the number of your chosen math-magic, or '4' to quit:")
		print("1. Integers")
		print("2. Fibonacci")
		print("3. Primes")
		print("4. Quit")
		choice = input("> ")

		try:
			if int(choice) > 0 and int(choice) < 5 :
				if choice != "4":
					print("")
					print("How many numbers do you want to generate?")
					self.count = int(input("> "))

				if choice == "1":
					res_int = self.generate_integers(self.count)
					self.print_results(res_int)

				if choice == "2":
					res_fib = self.generate_fibonacci(self.count)
					self.print_results(res_fib)

				if choice == "3":
					res_primes = self.generate_primes(self.count)
					self.print_results(res_primes)

				if choice != "4":
					self.show_menu()

			else:
		 		print("\nType 1, 2, 3, or 4. \n")
		 		self.show_menu()

		#handles non-int input
		except ValueError:
		 	print("\nType 1, 2, 3, or 4. \n")

	def print_results(self, res):
		for r in res:
			time.sleep(0.5)
			print(r)

	def generate_integers(self, count):
		int = [i for i in range(count)]
		return int

	def generate_fibonacci(self, count):
		fib_list = list()

		# the generator
		def fib():
			x, y = 0, 1
			indexer = 2

			yield x
			yield y

			while indexer < count:
				x, y = y, x + y
				yield y
				indexer += 1
				# fib_list.append(x)

		# create intstance of generator
		fib_inst = fib()
		# call next on generator (count) times, put result in fib_list
		for z in range(count):
			fib_list.append(next(fib_inst))

		return fib_list


	def generate_primes(self, count):
		w, x = 2, 1
		prime_list = list()

		while x <= count:
			isPrime = True
			for n in range(2, int(math.sqrt(w) + 1)):
				if w % n == 0:
					isPrime = False
					break

			if isPrime:
				prime_list.append(w)
				x += 1

			w += 1

		return prime_list

if __name__ == "__main__":
  magician = Mathmagician()
  magician.show_menu()

  # def generate_primes(self, count):
  #   i, x = 2, 1
  #   result = list()

  #   # x starts at 2 and ends at whatever the user typed in
  #   # for number of numbers to display
  #   while x <= count:

  #     # Start by assuming it is a prime number
  #     isPrime = True

  #     # Using the range 2...(square root of current number)
  #     for n in range(2, int(math.sqrt(i) + 1)):

  #       # If there is not a remainder with modulo calculation
  #       # then it's not a prime number
  #       if i % n == 0:
  #         isPrime = False
  #         break

  #     # Range loop is done, check if prime got negated
  #     # If not then we know it's a prime number
  #     if isPrime:
  #       result.append(i)
  #       x += 1

  #     i += 1

  #   return result

