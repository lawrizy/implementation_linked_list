class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = Node()
    def __str__(self):
        iter = self.head
        return_str = str(self.head.data)+'-->'
        while iter.next is not None:
            iter = iter.next
            return_str += str(iter.data) + '-->'
        return return_str
    def add_node(self,data):
        if (self.head.data is None):
            new_node = Node(data,None)
            self.head = new_node
        else:
            new_node = Node(self.head.data,self.head.next)
            self.head.data = data
            self.head.next = new_node

ll1 = LinkedList()
ll1.add_node("un")
ll1.add_node("deux")
ll1.add_node("trois")
print(ll1)