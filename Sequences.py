def seq1():
    count = 0

    for i in range(1, 500):
        if i % 2 != 0:
            print(i, end=" ")
            count += 1
            if count == 20:
                break


def seq2():
    count = 0
    for i in range(1, 500):
        if i % 2 == 0:
            print(i, end=" ")
            count += 1
            if count == 20:
                break


def seq3():
    count = 0
    for i in range(1, 500):
        if i % 2 != 0:
            print(i ** 2, end=" ")
            count += 1
            if count == 20:
                break


def seq4():
    count = 0
    for i in range(1, 500):
        if i % 2 == 0:
            print(i ** 2, end=" ")
            count += 1
            if count == 20:
                break


def seq6():
    count = 0
    for i in range(1, 500):
        if i % 2 != 0:
            print(i ** 3, end=" ")
            count += 1
        else:
            print(i, end=" ")
        if count == 20:
            break


def seq5():
    count = 0
    for i in range(1, 500):
        if i % 2 == 0:
            print(i * 2, end=" ")
            count += 1
        else:
            print(i, end=" ")
            count += 1
        if count == 20:
            break


seq1()
print()
seq2()
print()
seq3()
print()
seq4()
print()
seq5()
print()
seq6()
