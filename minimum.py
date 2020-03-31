def minimum(arr1):
    mini = arr1[0]
    for i in range(0, len(arr1)):
        if arr1[i] <= mini:
            mini = arr1[i]
    return mini


n = int(input())
arr = [int(x) for x in input().split()]
result = minimum(arr)
print(result)
