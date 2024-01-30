from code_challenges.trees.binary_tree import BinaryTree, Node
from code_challenges.stack_and_queue.stack_queue import Queue

def breadth_first(tree):
    list = []
    if not tree.root:
        return list
    queue = Queue()
    queue.enqueue(tree.root)

    while not queue.is_empty():
        node = queue.dequeue()
        list.append(node.data)

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

    return list
        