class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, root):
        if not root:
            return Node(key)
        else:
            if key < root.val:
                root.left = self.insert(key, root.left)
            else:
                root.right = self.insert(key, root.right)

        return root

    def _preorder(self, node):
        if node:
            print(node.val, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.val, end=" ")
            self._inorder(node.right)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.val, end=" ")

bst = BST()
input1 = 0

while input1 != -1:
    input1 = int(input("1 for insertion, 2 for inorder, -1 for exit"))
    
    if input1 == 1:
        ele = int(input("Enter a number"))
        bst.root = bst.insert(ele, bst.root)
    elif input1 == 2:
        print("Inorder traversal\n")
        bst._inorder(bst.root)
        print("\n")
