from collections import deque
n, H = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))

comb = sorted(zip(h, w))
h, w = zip(*comb)

h = list(h)
w = list(w)

l = 0
dq = deque()
min_inconvenience = float('inf')
cur_len = w[0]

for r in range(1,n):
    discomfort = abs(h[r]-h[r-1])

    while dq and dq[-1] < discomfort:
        dq.pop()
    dq.append(discomfort)

    cur_len += w[r]

    while cur_len >= H:
        max_diff = dq[0] if dq else 0
        min_inconvenience = min(min_inconvenience, max_diff)

        cur_len -= w[l]

        if r - l > 1 and abs(h[l+1] - h[l]) == dq[0]:
            dq.popleft()

        l+=1

if n == 1:
    min_inconvenience = 0
if max(w)>=H:
    min_inconvenience = 0

print(min_inconvenience)