import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
def sub_tree_size(v,edges):
    tree = defaultdict(list)
    for u,w in edges:
        tree[u].append(w)
        tree[w].append(u)

    sub_size = [0] * (v+1)
    visited = [False] * (v+1)

    def dfs(node):
        visited[node] = True
        size = 1

        for nk in tree[node]:
            if not visited[nk]:
                size += dfs(nk)
        sub_size[node] = size
        return size

    dfs(1)

    return sub_size[1:]

data = []
for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    data.append(line)


v = int(data[0])

edges = [tuple(map(int, line.split())) for line in data[1:]]

result = sub_tree_size(v,edges)
print(' '.join(map(str,result)))