from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10000000)
def find_tree_diameter_and_paths(n, edges):

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)


    def bfs(start):
        dist = [-1] * (n + 1)
        dist[start] = 0
        q = deque([start])
        farthest_node = start
        max_dist = 0
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)
                    if dist[neighbor] > max_dist:
                        max_dist = dist[neighbor]
                        farthest_node = neighbor
        return farthest_node, max_dist


    end1, _ = bfs(1)
    end2, diameter_length = bfs(end1)

    path = []
    parent = [-1] * (n + 1)

    def dfs_path(node, par):
        if node == end2:
            path.append(node)
            return True
        for neighbor in graph[node]:
            if neighbor != par:
                parent[neighbor] = node
                if dfs_path(neighbor, node):
                    path.append(node)
                    return True
        return False

    dfs_path(end1, -1)


    on_diameter = set(path)


    def max_subtree_depth(tree, node, parent):
        max_depth = 0
        for neighbor in tree[node]:
            if neighbor != parent:
                depth = max_subtree_depth(tree, neighbor, node)
                max_depth = max(max_depth, depth + 1)
        return max_depth

    def max_subtree_diameter(tree, node, parent):
        def bfs(start, allowed):
            dist = {}
            dist[start] = 0
            q = deque([start])
            farthest_node = start
            max_dist = 0
            while q:
                curr = q.popleft()
                for neighbor in tree[curr]:
                    if neighbor in allowed and neighbor not in dist:
                        dist[neighbor] = dist[curr] + 1
                        q.append(neighbor)
                        if dist[neighbor] > max_dist:
                            max_dist = dist[neighbor]
                            farthest_node = neighbor
            return farthest_node, max_dist


        def collect_subtree(curr, parent):
            subtree = {curr}
            for neighbor in tree[curr]:
                if neighbor != parent:
                    subtree.update(collect_subtree(neighbor, curr))
            return subtree


        allowed_nodes = collect_subtree(node, parent)


        farthest_node, _ = bfs(node, allowed_nodes)


        _, diameter = bfs(farthest_node, allowed_nodes)

        return diameter


    res = 0
    ready_diam_less_than_full = 0
    last = path[0]
    new_path = path[1:]
    diam_curr = 0

    for i, node in enumerate(new_path):
        temp = 0
        for neighbor in graph[node]:
            if neighbor not in on_diameter:

                res = max(res, (diameter_length * max_subtree_diameter(graph, neighbor, node)))
                res = max(res, ready_diam_less_than_full*(diameter_length - diam_curr - 1 + 1 + max_subtree_depth(graph, neighbor, node)))
                temp = max(temp, diam_curr + 2 + max_subtree_depth(graph, neighbor, node))

            elif neighbor == last:
                continue
            else:
                res = max(res, ready_diam_less_than_full * (diameter_length - diam_curr - 1))
                temp = max(temp, diam_curr + 1)
        diam_curr += 1
        ready_diam_less_than_full = max(ready_diam_less_than_full, temp)

    return res


n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

print(find_tree_diameter_and_paths(n, edges))
