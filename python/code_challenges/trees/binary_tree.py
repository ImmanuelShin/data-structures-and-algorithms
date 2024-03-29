class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self):
        if not self.root:
            raise ValueError("Nothing here")
        arr = []
        self._pre_order(self.root, arr)
        return arr

    def _pre_order(self, node, arr):
        if node == None:
            return
        arr.append(node.data)
        self._pre_order(node.left, arr)
        self._pre_order(node.right, arr)

    def in_order(self):
        if not self.root:
            raise ValueError("Nothing here")
        arr = []
        self._in_order(self.root, arr)
        return arr
        
    def _in_order(self, node, arr):
        if node == None:
            return
        self._in_order(node.left, arr)
        arr.append(node.data)
        self._in_order(node.right, arr)

    def post_order(self):
        if not self.root:
            raise ValueError("Nothing here")
        arr = []
        self._post_order(self.root, arr)
        return arr
    
    def _post_order(self, node, arr):
        if node == None:
            return
        self._post_order(node.left, arr)
        self._post_order(node.right, arr)
        arr.append(node.data)

    def get_max(self):
        if self.root is None:
            return float('-inf')
        max_val = self.root.data

        def search(node):
            nonlocal max_val
            if not node:
                return
            max_val = max(max_val, node.data)
            search(node.left)
            search(node.right)

        search(self.root)

        return max_val
            
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data