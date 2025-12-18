import sys
data = []
for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    data.append(line)
def build_parent_map(relationships):
    parent_map = {}
    for child, parent in relationships:
        parent_map[child] = parent
    return parent_map


def get_path_to_root(node, parent_map):
    path = []
    while node:
        path.append(node)
        node = parent_map.get(node)
    return path

def find_lca(node1, node2, parent_map):
    path1 = set(get_path_to_root(node1, parent_map))
    for ancestor in get_path_to_root(node2, parent_map):
        if ancestor in path1:
            return ancestor

n = int(data[0]) - 1


relationships = [line.split() for line in data[1:n+1]]
queries = [line.split() for line in data[n+1:]]

parent_map = build_parent_map(relationships)


result = []
for query in queries:
    if len(query) == 2:
        node1, node2 = query
        result.append(find_lca(node1, node2, parent_map))
    elif len(query) == 1:
        result.append(query[0])
print("\n".join(result))