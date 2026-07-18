def number_product(number):
    total = 1
    for i in range(len(number)):
        total *= int(number[i])
    print(total)

def main():
    n = input("Enter a number: ")
    print(f"The product of digits in {n} is : ",end= "")
    number_product(n)



main()