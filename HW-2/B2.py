n, k = list(map(int, input().split()))

numbers = list(map(int, input().split()))

prefix = {0: 1}
nowsum = 0
count = 0
for now in numbers:
    nowsum += now
    if (nowsum - k) in prefix:
        count += prefix[nowsum - k]

    if nowsum in prefix:
        prefix[nowsum] += 1
    else:
        prefix[nowsum] = 1

print(count)