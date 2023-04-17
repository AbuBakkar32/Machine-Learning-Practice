class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        curr_node = self.head
        prev_node = None

        while curr_node and curr_node.data != data:
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node:
            if prev_node:
                prev_node.next = curr_node.next
            else:
                self.head = curr_node.next

    def search(self, data):
        curr_node = self.head

        while curr_node and curr_node.data != data:
            curr_node = curr_node.next

        return curr_node
