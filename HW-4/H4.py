from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())

tree = defaultdict(list)
if N == 1:
    a = int(input())
    print(a, N)
    print(N)
    sys.exit(0)

for i in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

costs = list(map(int, input().split()))
dp = [0] * (N + 1)
dp_with = [0] * (N + 1)
visited = [False] * (N + 1)



def dfs_iterative(start):
    stack = [(start, -1)]
    order = []
    while stack:
        node, parent = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        order.append((node, parent))

        for neighbor in tree[node]:
            if not visited[neighbor]:
                stack.append((neighbor, node))
    return order



order = dfs_iterative(1)


for node, parent in reversed(order):
    dp[node] = 0
    dp_with[node] = costs[node - 1]

    for neighbor in tree[node]:
        if visited[neighbor]:
            dp[node] += dp_with[neighbor]
            dp_with[node] += min(dp[neighbor],
                                 dp_with[neighbor])


result = []
visited_restore = [False] * (N + 1)


def restore_iterative(start, parent_marked):
    stack = [(start, parent_marked)]

    while stack:
        node, parent_marked = stack.pop()
        if visited_restore[node]:
            continue
        visited_restore[node] = True
        if parent_marked:
            result.append(node)

        for neighbor in tree[node]:
            if not visited_restore[neighbor]:

                stack.append((neighbor, dp_with[neighbor] < dp[neighbor]) if parent_marked else (neighbor, True))


restore_iterative(1, dp_with[1] < dp[1])


total_cost = min(dp[1], dp_with[1])
print(total_cost, len(result))
print(" ".join(map(str, sorted(result))))
