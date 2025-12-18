n = int(input())

numbers = list(map(int, input().split()))
rev_numbers = numbers[::-1]
prefix = [0] * (n+1)
rev_prefix = [0] * (n+1)

pref = [0] * (n+1)
pref2 = [0] * (n+1)

for i in range(n):
    pref[i+1] = pref[i] + numbers[i]
    pref2[i + 1] = pref2[i] + rev_numbers[i]

for i in range(n):
    prefix[i + 1] = prefix[i] + numbers[i]
    prefix[i + 1] += pref[i]
    rev_prefix[i + 1] = rev_prefix[i] + rev_numbers[i]
    rev_prefix[i + 1] += pref2[i]

prefix = prefix[:-1]
rev_prefix = rev_prefix[:-1]

min_iter = float('inf')

for i in range(n):
    min_iter = min(min_iter, prefix[i]+rev_prefix[-(i+1)])
print(min_iter)