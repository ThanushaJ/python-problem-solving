Q1 = """Do you like Python?
1. yes
2. No"""
Q2 = """Do you like Python?
1. yes
2. No"""
Q3 = """Do you like Python?
1. yes
2. No"""
Q4 = """Do you like Python?
1. yes
2. No"""
Q5 = """Do you like Python?
1. yes
2. No"""

right = 0
wrong = 0
Que = (Q1, Q2, Q3, Q4, Q5)
Ans = (1, 1, 1, 1, 1)
#qDict = {'Q1': 1, "Q2": 1, "Q3": 1, "Q4": 1, "Q5": 1}
for i in range(0, 5):
    print(Que[i])
    A = int(input("Please select answer:  "))
    if A == Ans[i]:
        right += 1
    else:
        wrong += 1
# print("Right answers:  ", right)
# print("wrong answers:  ", wrong)
print("score = ", right)
