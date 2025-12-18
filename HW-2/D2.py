n, k = list(map(int, input().split()))

numbers = list(map(int, input().split()))

numbers.sort()
last = 0
max1 = 0
for first in range(len(numbers)):

    while last < n and numbers[last] - numbers[first] <= k:
        last +=1

    max1 = max(last - first, max1)

print(max1)