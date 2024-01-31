from code_challenges.trees.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(tree):
    def fizz_buzz(value):
        if value % 3 == 0 and value % 5 == 0:
            return "FizzBuzz"
        elif value % 3 == 0:
            return "Fizz"
        elif value % 5 == 0:
            return "Buzz"
        else:
            return str(value)
        
    def light_jog(node):
        new_nodes = [light_jog(child) for child in node.children]
        return Node(fizz_buzz(node.value), *new_nodes)
    
    new_root = light_jog(tree.root)
    return KaryTree(new_root)
