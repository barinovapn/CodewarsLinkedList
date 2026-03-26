class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None:
        raise Exception("Linked list is empty")
    if index < 0:
        raise Exception("Invalid index")

    current = node
    curr_index = 0
    while current:
        if curr_index == index:
            return current
        current = current.next
        curr_index += 1

    raise Exception("Index out of range")
