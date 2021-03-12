class Node():
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = Node()
    def add_node(self, data):
        if self.head.data == None:
            self.head.data = data
        else:
            new_node = Node()
            new_node.data = self.head.data
            new_node.next = self.head.next
            self.head.data = data
            self.head.next = new_node
    def __str__(self):
        return_string = ''
        current_node = self.head
        return_string = str(current_node.data)+'-->'
        while current_node.next is not None:
            current_node = current_node.next
            return_string += str(current_node.data)+' --> '

        return return_string

ll = LinkedList()
ll.add_node(1)
ll.add_node(3)
ll.add_node(5)
print(ll)
