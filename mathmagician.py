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
					print("Done!")

				if choice == "2":
					res_fib = self.generate_fibonacci(self.count)
					self.print_results(res_fib)
					print("Done!")

				if choice == "3":
					res_primes = self.generate_primes(self.count)
					self.print_results(res_primes)
					print("Done!")

				if choice != "4":
					# self.show_menu()
					self.quit()

			else:
		 		print("\nType 1, 2, 3, or 4. \n")
		 		self.show_menu()

		#handles non-int input
		except ValueError:
		 	print("\nType 1, 2, 3, or 4. \n")
		 	self.show_menu()

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


