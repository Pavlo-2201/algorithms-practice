n,b = map(int,input().split())
a = list(map(int,input().split()))

queue = 0
c = 0
for i in range(n):
    queue+=a[i]
    c += queue
    if queue>b:
        queue = queue - b
    else:
        queue = 0


print(c + queue)