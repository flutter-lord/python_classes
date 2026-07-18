def find_lcm(number):
    product = 1
    for i in range(len(number)):
        product *= number[i]
    print(product)


import math as m
def main():
    n = (input("Enter the numbers, separated by comma: ")).split(",")
    num = [int(x) for x in n]
main()