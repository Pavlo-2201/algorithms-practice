import sys
sys.setrecursionlimit(100000)
class TreeNode:
    def __init__(self, value,):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self,value):
        if self.root is None:
            self.root = TreeNode(value)
            return "DONE"
        return self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value == node.value:
            return "ALREADY"

        elif value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
                return "DONE"
            return self._add_recursive(node.left, value)

        else:
            if node.right is None:
                node.right = TreeNode(value)
                return "DONE"
            return self._add_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return "NO"
        if value == node.value:
            return "YES"
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def print_tree(self):
        result = []
        self._print_recursive(self.root, 0,result)
        return "\n".join(result)



    def _print_recursive(self, node,depth, result):
        if node is None:
            return
        self._print_recursive(node.left, depth+1, result)
        result.append("." * depth + str(node.value))
        self._print_recursive(node.right, depth+1, result)


data = []
for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    data.append(line)


tree = BinaryTree()
output = []

for command in data:
    parts = command.split()
    if parts[0] == "ADD":
        output.append(tree.add(int(parts[1])))
    elif parts[0] == "SEARCH":
        output.append(tree.search(int(parts[1])))
    elif parts[0] == "PRINTTREE":
        output.append(tree.print_tree())

print("\n".join(output))
