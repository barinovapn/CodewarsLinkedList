def loop_size(node):
    if node is None:
        return 0

    slow = node
    fast = node

    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    count = 1
    slow = slow.next
    while slow != fast:
        slow = slow.next
        count += 1

    return count
