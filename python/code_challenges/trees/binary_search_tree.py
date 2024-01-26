from code_challenges.trees.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):

    def add(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if data < node.data:
            if node.left:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def contains(self, data):
        if self.root == None:
            raise IndexError("Empty tree")
        return self._contains(data, self.root)
    
    def _contains(self, data, node):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._contains(data, node.left)
        elif data > node.data:
            return self._contains(data, node.right)