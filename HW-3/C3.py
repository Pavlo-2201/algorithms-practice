from collections import deque

n, k = map(int, input().split())
list_n = list(map(int, input().split()))
dq = deque()
ans = []

for i in range(n):

    if dq and dq[0] < i - k + 1:
        dq.popleft()

    while dq and list_n[dq[-1]] > list_n[i]:
        dq.pop()

    dq.append(i)
    if i >= k - 1:
        ans.append((list_n[dq[0]]))

for i in ans:
    print(i)