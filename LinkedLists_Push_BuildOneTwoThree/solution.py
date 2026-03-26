class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def push(head, data):
    """Додає новий вузол на початок linked list"""
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    """Будує linked list: 1 -> 2 -> 3 -> None"""
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
