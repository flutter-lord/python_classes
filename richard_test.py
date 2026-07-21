import random

class Rich:

	def __init__(self):
		number_length = int(input("Enter length of the length of the number: e.g 5 for 40986 e.t.c.: "))
		hidden_number = number_length * ["*"]

		self.__number_length = number_length
		self.__hidden_number = hidden_number

	def get_random_word(self):
		number = ""

		for i in range(self.__number_length):
			num = chr(random.randint(ord("0"), ord("9")))
			number += num
		return number