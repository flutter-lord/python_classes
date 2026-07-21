num1 = input("Enter the numbers in the first list, separated by comma: ").split(",")
list1 = [int(i) for i in num1]

num2 = input("Enter the numbers in the second list, separated by comma: ").split(",")
list2 = [int(j) for j in num2]

list3 = list1 + list2
list3.sort()
print(f"The merge list is :", end= " ")
for k in list3:
	print(k, end= " ")