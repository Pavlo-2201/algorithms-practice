n, k = list(map(int, input().split()))

numbers = list(map(int, input().split()))
count = 0
last = 0
for first in range(n):
    while last < n and numbers[last] - numbers[first] <= k:
        last+=1
    count += n - last
print(count)