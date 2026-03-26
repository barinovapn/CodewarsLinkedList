class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s: str):
    """Створює LinkedList з рядка формату '0 -> 1 -> 2 -> None'"""
    if s == "None":
        return None

    values = s.split(" -> ")
    values = [int(v) for v in values if v != "None"]

    head = None
    current = None
    for val in values:
        node = Node(val)
        if not head:
            head = node
            current = node
        else:
            current.next = node
            current = node
    return head
