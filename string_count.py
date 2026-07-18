s =  input("Enter the scores separated by commas: ").split()
sentence = [x for x in s]
sentence.sort()
for i in range(len(sentence)):
    if sentence[i] == sentence[i - 1]:
        continue
    print(f"{sentence[i]} : {sentence.count(sentence[i])}")