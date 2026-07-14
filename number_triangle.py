def triangle(number):
    total = 0
    i = 1
    while i < number:
        if total == number:
            print(f"{total} is a triangular number")
            break
        total += i
    i += 1




def main():
    n = int(input("Enter a number to check if it\'s a triangle number: "))
    triangle(n)

main()