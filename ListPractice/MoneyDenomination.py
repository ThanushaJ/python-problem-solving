i = 0
money = []
NotesList = []
Notes = {2000: 0, 1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
number = int(input())
rem = 0
quo = 0


def MatchNotes(money, NotesList):
    print("money", money)
    lengthNotes = len(NotesList)
    for j in range(lengthNotes-1):
        if money < NotesList[j]:
            rem = money % NotesList[j - 1]
            quo = money // NotesList[j - 1]
            money = rem
            Notes[NotesList[j-1]] += quo
            print("quo", quo)
            print("rem", rem)
            print(Notes[NotesList[j-1]])
            break
        elif money > NotesList[lengthNotes-1]:
            newRem = money % NotesList[lengthNotes-1]
            numQuo = money // NotesList[lengthNotes-1]
            print("numQuo", numQuo)
            Notes[NotesList[lengthNotes-1]] +=numQuo
            print(newRem)
            print(Notes)
            if newRem!=0:
                #print("newRem", newRem)
                #print("oldValue", Notes[NotesList[lengthNotes-2]])
                Notes[NotesList[lengthNotes-2]] += 1
                break
    return money


def countMoney(money, NotesList):
    for i in range(len(money)):
        if money[i] in NotesList:
            Notes[money[i]] += 1
        else:
            getRet = MatchNotes(money[i], NotesList)
            money[i] = getRet
            MatchNotes(money[i], NotesList)

while number > 0:
    rem = number % 10
    money.append(rem * 10 ** i)
    number = number // 10
    i += 1
money = sorted(money)
print(money)
NotesList = list(Notes.keys())
NotesList = sorted(NotesList)
print(NotesList)
countMoney(money,NotesList)
print(Notes)
