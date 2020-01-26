repList = []
checked = []
n = int(input())
inputList = [int(x) for x in input().split()]
iLength = len(inputList)
count = 0
for i in range(0, iLength):
    for j in range(0, iLength):
        if inputList[j] == inputList[i] and inputList[j] not in checked:
            if (j != i):
                repList.append(inputList[i])
                #checked.append(inputList[i])

checked = set(repList)
newchecked = list(checked)
repLength = len(checked)
print(checked)
if repLength != 0:
    for i in range(repLength):
        print(newchecked[i])
else:
    print("The list is empty")