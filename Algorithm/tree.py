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
