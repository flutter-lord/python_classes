l1 = input("Enter the first list, separated them by commas: ").split(",")
list1 = [int(x) for x in l1]

l2 = input("Enter the second list, separated them by commas: ").split(",")
list2 = [int(y) for y in l2]
print("The common integers between list1 and list2 are : ", end= "")
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            print(list1[i], end= " ")