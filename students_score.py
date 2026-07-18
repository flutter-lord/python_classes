s = input("Enter the students score separated by comma: ").split(",")
scores = [int(i) for i in s]
a = 0
b = 0
c = 0
d = 0
f = 0

for score in scores:
    if score >= 90:
        a+= 1

    elif score >= 80:
        b +=  1

    elif score >= 70:
        c+= 1

    elif score >= 60:
        d+= 1

    else:
        f+= 1