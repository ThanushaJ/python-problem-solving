name = "thanusha"
nameList = list(name)
print(nameList)
setList = set(nameList)
print(setList)
for i in setList:
    for j in range(len(nameList)):
        if nameList[j] == i: