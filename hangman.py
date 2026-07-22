import random

import sys

class HangMan:

	def __init__(self):
		self.__word_list = ["helob", "maize", "god", "royland", "write", "trash", "period"]
		self.__word = random.choice(self.__word_list)
		self.__hidden = ["*"]  * len(self.__word)

	def get_word(self):
		return self.__word

	def guess_word(self):
		while self.__hidden != list(self.__word):
			guess = input(f"Guess a letter in this word {"".join(self.__hidden)}: ").lower()

			while guess in self.__word:
				self.__hidden[self.get_word().index(guess)] = guess
				guess = input(f"Guess a letter in this word  {"".join(self.__hidden)}: ").lower()

				if self.__hidden == list(self.__word):
					print(f"Your word is {self.__word}\nThank your for participating in the game !!!!!")
					sys.exit()