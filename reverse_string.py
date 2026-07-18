import random
s = list(input("Enter your string: "))
random.shuffle(s)
for i in range(len(s)):
    print(s[i], end=" ")