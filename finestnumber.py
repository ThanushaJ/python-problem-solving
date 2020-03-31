def FinestNum(number):
    if(number > 0):
        for t in range(1,number):
            cube = t**3
            t2 = t + 1
            cube1 = t2**3
            total = cube + cube1
            if(total == number):
                return number
            break


z = int(input())
arr = [int(x) for x in input().split()]
finestNumbers = []
for i in range(0, z):
    f = FinestNum(arr[i])
    if(f == arr[i]):
        finestNumbers.append(f)

finestNumbers = sorted(finestNumbers)
if(len(finestNumbers) >= 1):
    for i in finestNumbers:
        print(i, end=' ')
else:
    num = -1
    print(num)
