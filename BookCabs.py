EP = int(input("End Point"))
SP = int(input("Start Point"))
Distance = EP - SP
PriceList = {"Mini": 10, "Micro": 12, "Prime": 15}
CabsCount = {"Mini": 2, "Micro": 2, "Prime": 2}
print(CabsCount)
SelectCab = str(input("Select Cab"))
while SelectCab != 'Q':
    while CabsCount[SelectCab] != 0:
        TotalPrice = Distance * PriceList[SelectCab]
        print("Total Price", TotalPrice)
        CabsCount[SelectCab] -= 1
        print(CabsCount)
        EP = int(input("End Point"))
        SP = int(input("Start Point"))
        Distance = EP - SP
        SelectCab = input("Select Cab in While inner")
    if CabsCount[SelectCab] == 0:
        print("Cab Category not available")
        print(CabsCount)
        EP = int(input("End Point"))
        SP = int(input("Start Point"))
        Distance = EP - SP
        SelectCab = input("Select Cab in else")


