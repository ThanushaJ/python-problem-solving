def GreatNumber(number):
    nums = []
    prod = 1
    sums = 0
    N1 = number
    while number > 0:
        d = number % 10
        number = number // 10
        nums.append(d)
    for i in nums:
        sums += i
        prod *= i
    total = sums + prod
    if total == N1:
        return "Great"
    else:
        return "no"


n = int(input())
result = GreatNumber(n)
print(result)
