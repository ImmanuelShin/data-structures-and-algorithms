import pytest
from code_challenges.trees.binary_tree import BinaryTree, Node

def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.get_max()
    expected = 30

    assert actual == expected

def test_max_val_negative_numbers():
    tree = BinaryTree()
    tree.root = Node(-5)
    tree.root.left = Node(-10)
    tree.root.right = Node(-3)

    actual = tree.get_max()
    expected = -3

    assert actual == expected

def test_max_val_empty_tree():
    tree = BinaryTree()

    actual = tree.get_max()
    expected = float('-inf')

    assert actual == expected