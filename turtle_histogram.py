import random

def random_lowercase():
	list_characters = []
	for i in range(1000):
		lowercase = chr(random.randint(ord("a"), ord("z")))
		list_characters.append(lowercase)
	return list_characters

def count_letters():
	list_count = []
	for letter in range(ord("a"), ord("z") + 1):
		count = random_lowercase().count(chr(letter))
		list_count.append(count)
	return list_count

def main():
	print(len(random_lowercase()))
	print("")
	print(len(count_letters()))
	print("")
	print(sum(count_letters()))

main()