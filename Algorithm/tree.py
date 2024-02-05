class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            curr_node = self.root

            while True:
                if data < curr_node.data:
                    if curr_node.left is None:
                        curr_node.left = new_node
                        break
                    else:
                        curr_node = curr_node.left
                else:
                    if curr_node.right is None:
                        curr_node.right = new_node
                        break
                    else:
                        curr_node = curr_node.right

    def search(self, data):
        curr_node = self.root

        while curr_node and curr_node.data != data:
            if data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        return curr_node

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data)
            self.inorder_traversal(node.right)


if __name__ == '__main__':
    bst = BinarySearchTree()

    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(4)

    bst.inorder_traversal(bst.root)  # Output: 2 3 4 5 8

    node = bst.search(3)
    print(node.data)  # Output: 3


#  Data Structure Tree Implementation in Python

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, data):
#         if self.root is None:
#             self.root = Node(data)
#         else:
#             self._insert(data, self.root)
#
#     def _insert(self, data, node):
#         if data < node.data:
#             if node.left is None:
#                 node.left = Node(data)
#             else:
#                 self._insert(data, node.left)
#         else:
#             if node.right is None:
#                 node.right = Node(data)
#             else:
#                 self._insert(data, node.right)
#
#     def inorder_traversal(self):
#         if self.root is not None:
#             self._inorder_traversal(self.root)
#
#     def _inorder_traversal(self, node):
#         if node:
#             self._inorder_traversal(node.left)
#             print(node.data, end=" ")
#             self._inorder_traversal(node.right)
#
#
# # Create a tree
# tree = Tree()
# tree.insert(5)
# tree.insert(3)
# tree.insert(7)
# tree.insert(2)
# tree.insert(4)
# tree.insert(6)
# tree.insert(8)
#
# # Print the inorder traversal
# print("Inorder traversal:")
# tree.inorder_traversal() # Output: 2 3 4 5 6 7 8

