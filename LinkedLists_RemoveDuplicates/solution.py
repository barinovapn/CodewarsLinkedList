class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None

    seen = set()
    current = head
    seen.add(current.data)

    while current.next:
        if current.next.data in seen:

            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next

    return head
