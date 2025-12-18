from collections import deque, defaultdict
import sys
class DisjointSetUnion:
    def __init__(self, size):
        self.roots = list(range(size))
        self.heights = [0] * size

    def find(self, bird):
        if self.roots[bird] != bird:
            self.roots[bird] = self.find(self.roots[bird])
        return self.roots[bird]

    def merge(self, bird1, bird2):
        root1 = self.find(bird1)
        root2 = self.find(bird2)
        if root1 != root2:
            if self.heights[root1] > self.heights[root2]:
                self.roots[root2] = root1
            elif self.heights[root1] < self.heights[root2]:
                self.roots[root1] = root2
            else:
                self.roots[root2] = root1
                self.heights[root1] += 1


class Woodpecker:
    def __init__(self, id):
        self.id = id
        self.neighbors = []


def separate_bipartite_subsets(woodpecker_group, tree_structure):
    coloring = {}
    current_level = set()
    next_level = set()
    initial_woodpecker = next(iter(woodpecker_group))
    coloring[initial_woodpecker] = 0
    for neighbor in initial_woodpecker.neighbors:
        current_level.add(neighbor)
    current_color = 1
    while current_level:
        for woodpecker in current_level:
            if woodpecker in coloring and coloring[woodpecker] != current_color:
                return False
            elif woodpecker not in coloring:
                for neighbor in woodpecker.neighbors:
                    next_level.add(neighbor)
                coloring[woodpecker] = current_color
        current_level, next_level = next_level, set()
        current_color = 1 - current_color

    tree1, tree2 = tree_structure
    for woodpecker in woodpecker_group:
        if coloring[woodpecker] == 0:
            tree1.add(woodpecker)
        elif coloring[woodpecker] == 1:
            tree2.add(woodpecker)

    return True


def calculate_placement_variants(tree_structure, modulo):
    total_variants = 1
    tree1, tree2 = tree_structure
    if len(tree1) == 1 and len(tree2) == 1:
        return 2
    root_woodpecker = None
    for woodpecker in tree1:
        if len(woodpecker.neighbors) > 1:
            root_woodpecker = woodpecker
            break
    if not root_woodpecker:
        tree1, tree2 = tree2, tree1
        for woodpecker in tree1:
            if len(woodpecker.neighbors) > 1:
                root_woodpecker = woodpecker
                break

    woodpecker_stack = deque([root_woodpecker])
    next_stack = deque()
    current_tree = {root_woodpecker}
    alternate_tree = set()
    swap_count = 0
    intermediate_woodpeckers = []
    single_neighbor_count = 0
    for neighbor in woodpecker_stack[0].neighbors:
        if len(neighbor.neighbors) == 1:
            if neighbor not in alternate_tree:
                single_neighbor_count += 1
                total_variants *= single_neighbor_count
                total_variants %= modulo
            next_stack.appendleft(neighbor)
            alternate_tree.add(neighbor)
        else:
            intermediate_woodpeckers.append(neighbor)
    if len(intermediate_woodpeckers) > 2:
        print(0)
        sys.exit(0)
    elif len(intermediate_woodpeckers) == 2:
        next_stack.appendleft(intermediate_woodpeckers[0])
        next_stack.append(intermediate_woodpeckers[1])
        alternate_tree.add(intermediate_woodpeckers[0])
        alternate_tree.add(intermediate_woodpeckers[1])
    elif len(intermediate_woodpeckers) == 1:
        next_stack.append(intermediate_woodpeckers[0])
        alternate_tree.add(intermediate_woodpeckers[0])

    swap_count += 1
    woodpecker_stack, next_stack = next_stack, woodpecker_stack
    current_tree, alternate_tree = alternate_tree, current_tree

    while len(woodpecker_stack[0].neighbors) != 1:
        intermediate_woodpeckers = []
        single_neighbor_count = 0
        for neighbor in woodpecker_stack[0].neighbors:
            if len(neighbor.neighbors) == 1:
                if neighbor not in alternate_tree:
                    single_neighbor_count += 1
                    total_variants *= single_neighbor_count
                    total_variants %= modulo
                next_stack.appendleft(neighbor)
                alternate_tree.add(neighbor)
            else:
                intermediate_woodpeckers.append(neighbor)
        if len(intermediate_woodpeckers) > 2:
            print(0)
            sys.exit(0)
        elif len(intermediate_woodpeckers) == 2:
            if intermediate_woodpeckers[0] in alternate_tree and intermediate_woodpeckers[1] in alternate_tree:
                print(0)
                sys.exit(0)
            elif intermediate_woodpeckers[0] in alternate_tree:
                next_stack.appendleft(intermediate_woodpeckers[1])
                alternate_tree.add(intermediate_woodpeckers[1])
            else:
                next_stack.appendleft(intermediate_woodpeckers[0])
                alternate_tree.add(intermediate_woodpeckers[0])

        swap_count += 1
        woodpecker_stack, next_stack = next_stack, woodpecker_stack
        current_tree, alternate_tree = alternate_tree, current_tree

    if swap_count % 2 == 0:
        woodpecker_stack, next_stack = next_stack, woodpecker_stack
        current_tree, alternate_tree = alternate_tree, current_tree

    while len(woodpecker_stack[-1].neighbors) != 1:
        intermediate_woodpeckers = []
        single_neighbor_count = 0
        for neighbor in woodpecker_stack[-1].neighbors:
            if len(neighbor.neighbors) == 1:
                if neighbor not in alternate_tree:
                    single_neighbor_count += 1
                    total_variants *= single_neighbor_count
                    total_variants %= modulo
                next_stack.append(neighbor)
                alternate_tree.add(neighbor)
            else:
                intermediate_woodpeckers.append(neighbor)
        if len(intermediate_woodpeckers) > 2:
            print(0)
            sys.exit(0)
        elif len(intermediate_woodpeckers) == 2:
            if intermediate_woodpeckers[0] in alternate_tree and intermediate_woodpeckers[1] in alternate_tree:
                print(0)
                sys.exit(0)
            elif intermediate_woodpeckers[0] in alternate_tree:
                next_stack.append(intermediate_woodpeckers[1])
                alternate_tree.add(intermediate_woodpeckers[1])
            else:
                next_stack.append(intermediate_woodpeckers[0])
                alternate_tree.add(intermediate_woodpeckers[0])

        woodpecker_stack, next_stack = next_stack, woodpecker_stack
        current_tree, alternate_tree = alternate_tree, current_tree

    if len(tree1) == 1 or len(tree2) == 1:
        return 2 * total_variants
    return 4 * total_variants


def assemble_woodpecker_groups(all_woodpeckers):
    num_woodpeckers = len(all_woodpeckers)
    dsu_structure = DisjointSetUnion(num_woodpeckers)

    for woodpecker in all_woodpeckers:
        for neighbor in woodpecker.neighbors:
            dsu_structure.merge(woodpecker.id, neighbor.id)

    group_mapping = defaultdict(set)
    for woodpecker in all_woodpeckers:
        root_id = dsu_structure.find(woodpecker.id)
        group_mapping[root_id].add(woodpecker)

    return list(group_mapping.values())



num_woodpeckers, num_pairs, modulo_val = map(int, input().split())
woodpecker_list = [Woodpecker(i) for i in range(num_woodpeckers)]

for _ in range(num_pairs):
    bird1, bird2 = map(int, input().split())
    bird1 -= 1
    bird2 -= 1
    woodpecker_list[bird1].neighbors.append(woodpecker_list[bird2])
    woodpecker_list[bird2].neighbors.append(woodpecker_list[bird1])

grouped_woodpeckers = assemble_woodpecker_groups(woodpecker_list)

large_groups_count = 0
for group in grouped_woodpeckers:
    if len(group) != 1:
        large_groups_count += 1

forest_graphs = [(set(), set()) for _ in range(large_groups_count)]
processed_groups = 0
for group in grouped_woodpeckers:
    if len(group) != 1:
        if not separate_bipartite_subsets(group, forest_graphs[processed_groups]):
            print(0)
            sys.exit(0)
        processed_groups += 1

result_variants = 1
for tree_data in forest_graphs:
    result_variants *= calculate_placement_variants(tree_data, modulo_val)
    result_variants %= modulo_val

cnt_more_than_one_person = sum(1 for group in grouped_woodpeckers if len(group) > 1)
for i in range(2, cnt_more_than_one_person + 1):
    result_variants  *= i
    result_variants  %=modulo_val

cnt = sum(len(group) if len(group) != 1 else 0 for group in grouped_woodpeckers)
introverts =  num_woodpeckers - cnt

for i in range(introverts):
    result_variants *= (cnt + 2 + i) % modulo_val
    result_variants %= modulo_val

print( result_variants )