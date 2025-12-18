n = int(input())
chick = list(map(int, input().split()))


prefix = [0] * (n+1)
for i in range(n):
    prefix[i+1] += prefix[i] + chick[i]

print(" ".join(map(str, prefix[1:])))