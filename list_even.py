def is_even(my_list):
	even = True
	for elements in my_list:
		if elements % 2 != 0:
			even = False
			break
		else:
			even = True

	if even == True:
		print("All the elements in the list are even")

	else:
		print("The elements in the list contains odd")

def main():
	n = input("Enter all the numbers in the list separated by comma: ").split(",")
	number = [int(x) for x in n]
	is_even(number)
main()