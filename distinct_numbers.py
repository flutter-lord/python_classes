n = input("Enter any ten numbers, separated by commas: ").split(",")
number = [x for x in n]
#number.sort()

distinct_numbers = []
for i in range(len(number)):
    if (number[i] in distinct_numbers) == True:
        continue
    distinct_numbers.append(number[i])
print(f"The number of distinct numbers : {len(distinct_numbers)}")
print(f"The distinct numbers are : {distinct_numbers}")