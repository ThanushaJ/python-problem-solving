def add(a, b):
    return a + b


def sub(a, b):
    if a > b:
        return a - b
    else:
        return b - a


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


a = 10
b = 20
Need = "yes"
while Need == "yes":
    print("select operation \n 1.add\n2.sub\n3.mul\n4.div")
    choice = int(input())
    a = int(input("input1: "))
    b = int(input("input2  "))
    if choice == 1:
        print("The sum of",a,"and",b,"is",add(a,b))
    if choice == 2:
        print("The difference of",a,"and",b,"is",sub(a,b))
    if choice == 3:
        print("The product of",a,"and",b,"is",mul(a,b))
    if choice == 4:
        print("The quotient of",a,"/",b,"is",div(a,b))
    print("do you want to continue (yes/no)")
    Need = input()

