import sys

def find_search(my_search, number):
    number_length = len(number)
    mid = number_length // 2 + 1

    if number[mid] == my_search:
        print(f"The number {my_search} you searched is at {mid} place of the sequence")
        sys.exit()

    else:
        if my_search < number[mid]:
            number = list(number[0: mid])

        elif my_search > number[mid]:
            number = list(number[mid + 1:])

        else:
            print(f"Your search is at {mid + 1} place of the sequence")
            sys.exit()

def main():
    #n = [10, 0, 6, 2, 7, 4, 8, 1, 5, 9, 6]
    n = [1,2,3,4,5,6,7,8,9,10,11]
    m = eval(input(f"Input your search: "))
    if m in n:
        find_search(m, n)

    else:
        print("Your search is not found")

main()