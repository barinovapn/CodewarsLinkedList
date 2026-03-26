class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def stringify(node):
    """Перетворює зв’язаний список у рядок"""
    if not node:
        return 'None'
    values = []
    current = node
    while current:
        values.append(str(current.data))
        current = current.next
    values.append('None')

    return " -> ".join(values)
