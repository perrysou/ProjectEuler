class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Insert(head, data):
    while not head:
        nextnode = Node(data)
        head.next = nextnode

head = Node

data = int(raw_input().strip())

Insert(head, data)



