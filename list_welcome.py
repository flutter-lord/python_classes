import statistics as st

NUMBER_OF_ELEMENTS = int(input("How many elements do you want to enter?: "))
list_number = []

for i in range(1, NUMBER_OF_ELEMENTS + 1):
    number = eval(input(f"Enter num{i} : "))
    list_number.append(number)

avg = st.mean(list_number)
print(f"The average number is {avg : .3f}")

above_avg = [x for x in list_number if x > avg]
print(f"The number of elements above the average is {len(above_avg)}")