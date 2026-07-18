import  statistics as st
scores = list(eval(input("Enter the scores separated by comma: ")))
average_score = st.mean(scores)
print(f"Average score is {average_score}")
print("Pass / Fail Status: ")

for i in range(len(scores)):
    status = "Fail" if scores[i] < average_score else "Pass"
    print(f"score {scores[i]} --> {status}")