def gdc(number):
    divisor = 2
    while divisor <= number:
        print(divisor)





def main():
    n = input("Input the list of numbers, separated by comma: ").split(",")
    number = [int(x) for x in n]
    gdc(number)