def sumPairs(num):
    pair = 0
    for i in range(1, num):
        for j in range(1, num):
            if j + i == num:
                pair += 1
    return pair


n = int(input())
result = sumPairs(n)
print(result)