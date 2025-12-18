MOD = 10**9 + 7
def add_edge(graph, src, dest, weight):
    graph[src].append((dest, weight))

def dfs(node, parent, graph, sizes, f, sum_f, comb):
    sizes[node] = f[node][0] = 1
    for neighbor, weight in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, graph, sizes, f, sum_f, comb)
            limit = sizes[node] + sizes[neighbor]
            g = [0] * limit
            if weight == 1:
                for j in range(sizes[node]):
                    for k in range(sizes[neighbor] + 1):
                        tmp1 = (f[node][sizes[node] - j - 1] % MOD *
                                (sum_f[neighbor][sizes[neighbor] - 1] - sum_f[neighbor][sizes[neighbor] - k - 1] + MOD) % MOD)
                        tmp2 = (comb[j + k][k] * comb[limit - j - k - 1][sizes[neighbor] - k] % MOD)
                        g[limit - j - k - 1] = (g[limit - j - k - 1] + tmp1 * tmp2 % MOD) % MOD
            else:
                for j in range(sizes[node]):
                    for k in range(sizes[neighbor] + 1):
                        tmp1 = f[node][j] % MOD * sum_f[neighbor][k - 1] % MOD
                        tmp2 = comb[j + k][k] * comb[limit - j - k - 1][sizes[neighbor] - k] % MOD
                        g[j + k] = (g[j + k] + tmp1 * tmp2 % MOD) % MOD
            sizes[node] += sizes[neighbor]
            for j in range(sizes[node]):
                f[node][j] = g[j]
    sum_f[node][0] = f[node][0]
    for j in range(1, sizes[node]):
        sum_f[node][j] = (sum_f[node][j - 1] + f[node][j]) % MOD

def mod_pow(base, exp, mod):
    result = 1
    while exp:
        if exp % 2:
            result = result * base % mod
        base = base * base % mod
        exp //= 2
    return result

def comb_mod(n, k, mod):
    if n < k:
        return 0
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = numerator * (n - i) % mod
        denominator = denominator * (i + 1) % mod
    return numerator * mod_pow(denominator, mod - 2, mod) % mod

def main():
    n = int(input())
    comb = [[0] * n for _ in range(n)]
    for i in range(n):
        comb[i][0] = 1
        for j in range(1, i + 1):
            comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % MOD
    graph = [[] for _ in range(n + 1)]
    sizes = [0] * (n + 1)
    f = [[0] * (n + 1) for _ in range(n + 1)]
    sum_f = [[0] * (n + 1) for _ in range(n + 1)]
    for __ in range(n - 1):
        a, b = map(int, input().split())
        add_edge(graph, b, a, 1)
        add_edge(graph, a, b, -1)
    dfs(1, 0, graph, sizes, f, sum_f, comb)
    answer = sum(f[1][:n]) % MOD
    print(answer * comb_mod(n, n, MOD) % MOD)


if __name__ == "__main__":
    main()
