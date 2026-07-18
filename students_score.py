s = input("Enter the students score separated by comma: ").split(",")
scores = [int(i) for i in s]
grade = []

for j in range(len(scores)):
    if scores[j] >= 90:
        grade.append("A")

    elif scores[j] >= 80:
        grade.append("B")

    elif scores[j] >= 70:
        grade.append("C")

    elif scores[j] >= 60:
        grade.append("D")

    else:
        grade.append("F")
grade.sort()

for k in range(len(grade)):
    if grade[k] == grade[k- 1]:
        continue
    print(f"{grade[k]} : {grade.count(grade[k])}")