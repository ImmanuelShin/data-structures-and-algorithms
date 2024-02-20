from code_challenges.trees.binary_tree import BinaryTree

def tree_intersection(tree1, tree2):
    seen1 = set()
    seen2 = set()
    def walk(node, is_first_tree):
        if not node:
            return
        if is_first_tree:
            seen1.add(node.data)
        elif node.data in seen1:
            seen2.add(node.data)
        walk(node.left, is_first_tree)
        walk(node.right, is_first_tree)

    walk(tree1.root, True)
    walk(tree2.root, False)
    return seen2