n = input("Enter all the numbers in the list separated by comma: ").split(",")
number = [int(x) for x in n]

for elements in number:
	print(elements, end= "")