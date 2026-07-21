import random

class Rich:

	def __init__(self):
		number_length = int(input("Enter length of the length of the number: e.g 5 for 40986 e.t.c.: "))
		hidden_number = number_length * "*"
		your_guess = input(f"Enter a number you guess in {hidden_number}: ")

		self.__number_length = number_length
		self.__your_guess = your_guess
		self.__hidden_number = hidden_number

	def get_random_word(self):
		number = ""

		for i in range(self.__number_length):
			number = chr(random.randint(ord("0"), ord("9")))
			number += number
		print(number)
		return number

	def display_word(self):
		while self.__hidden_number != self.get_random_word():
			while self.__your_guess in self.get_random_word():
				self.__hidden_number[self.get_random_word().index(self.__your_guess)] = self.__your_guess
				self.__your_guess = input(f"Enter a number you guess in {self.__hidden_number}: ")

			else:
				self.__your_guess = input(f"Enter a number you guess in {self.__hidden_number}: ")
		return self.__hidden_number