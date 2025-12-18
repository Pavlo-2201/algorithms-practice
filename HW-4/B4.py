import sys

sys.setrecursionlimit(100000)

n = int(input())
parent_map = {}
all_people = set()
has_parent = set()
for _ in range(n - 1):
        child, parent = input().split()
        if parent not in parent_map:
            parent_map[parent] = []
        parent_map[parent].append(child)
        all_people.add(child)
        all_people.add(parent)
        has_parent.add(child)

root = (all_people - has_parent).pop()

count = {}

def count_leaf(node,parent_map,count):
    if node not in parent_map or not parent_map[node]:
        count[node] = 0
        return 0
    k = 0
    for child in parent_map[node]:
        k += 1 + count_leaf(child,parent_map,count)
    count[node] = k
    return count[node]

count_leaf(root,parent_map,count)

sorted_nodes = sorted(all_people)
for node in sorted_nodes:
    print(node,count.get(node,0))
