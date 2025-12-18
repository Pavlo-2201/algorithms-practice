import sys
sys.setrecursionlimit(1000000)
def calculate_coins(n, managers):

    tree = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        tree[managers[i - 2]].append(i)

    coins = [0] * (n + 1)

    def dfs(node):
        total_coins = 0
        num_subordinates = 0


        for child in tree[node]:
            child_coins, child_subordinates = dfs(child)
            total_coins += child_coins
            num_subordinates += child_subordinates + 1


        coins[node] = total_coins + num_subordinates + 1
        return coins[node], num_subordinates


    dfs(1)

    return coins[1:]



n = int(input())
managers = list(map(int, input().split()))

result = calculate_coins(n, managers)


print(*result)