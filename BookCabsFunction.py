fare = {"Mini": 10, "Micro": 12, "Prime": 15}
cabsCount = {"Mini": ['c1', 'c2', 'c3'], "Micro": ['c1', 'c2', 'c3'], "Prime": ['c1', 'c2', 'c3']}
totalFare = 0


def Available(count):
    cabs = 0
    for x in count:
        cabs += len(count[x])
    return cabs


def BookCab():
    print(cabsCount)
    start = int(input("Start Point  "))
    end = int(input("End Point  "))
    distance = end - start
    option = input("Select a cab  ")
    if len(cabsCount[option]) > 0:
        totalFare = distance * fare[option]
        print("Total Fare   ", totalFare)
        cabIndex = len(cabsCount[option]) - 1
        print("Cab Details  ", cabsCount[option][cabIndex])
        cabsCount[option].pop()
    else:
        print("Cabs not available in this category")


# print(Available(CabsCount))

while Available(cabsCount) != 0:
    print("Do you want to book a cab (yes/no):  ")
    need = input()
    if need == 'yes':
        print("Please book your cab")
        BookCab()
    elif need == 'no':
        print("Bye, Please come back when you need cabs")
        break

else:
    print("Cabs not available for the day, See you tomorrow!!")
