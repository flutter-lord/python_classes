def binary_search(lst, key):
    low = 0
    high = len(lst) - 1

    while high >= low:
        mid = (high + low) // 2
        if key < lst[mid]:
            high = mid - 1

        elif key == lst[mid]:
            return mid

        else:
            low = mid + 1
    return -low - 1

def main():
    x = [-3, 1, 2, 4, 9, 23]
    print(binary_search(x, 4))

main()