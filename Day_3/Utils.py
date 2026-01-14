

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_list(head):
    if head is None:
        print("empty list")
        return
    walker = head
    while walker is not None:
        print(walker.value)
        walker = walker.next


def insert_sorted(head, x):
    """
    Insert value x into a singly linked list while keeping it sorted (ascending).
    Duplicates are placed AFTER existing equal values (stable).
    Returns the (possibly new) head.
    """
    new_node = Node(x)

    # Empty list or insert at the very front
    if head is None or x < head.value:
        new_node.next = head
        return new_node

    # Walk until we find a place where current.next.value >= x
    # This ensures we insert AFTER existing equals (<=).
    prev = head
    curr = head.next
    while curr is not None and curr.value <= x:
        prev = curr
        curr = curr.next

    # Insert between prev and curr
    prev.next = new_node
    new_node.next = curr
    return head


def delete_value(head, x):
    """
    Delete the FIRST occurrence of value x from the list.
    Returns the (possibly new) head.
    """
    if head is None:
        return None

    # If the head holds the value
    if head.value == x:
        return head.next  # drop the head

    # Otherwise, search for the node to delete
    prev = head
    curr = head.next
    while curr is not None and curr.value != x:
        prev = curr
        curr = curr.next

    # Not found
    if curr is None:
        return head

    # Unlink the node
    prev.next = curr.next
    return head


def delete_all(head, x):
    """
    (Optional) Delete ALL occurrences of x.
    Returns the (possibly new) head.
    """
    # Remove at front repeatedly
    while head is not None and head.value == x:
        head = head.next

    # Now remove in the rest
    prev = head
    curr = head.next if head is not None else None
    while curr is not None:
        if curr.value == x:
            prev.next = curr.next
            curr = prev.next
        else:
            prev = curr
            curr = curr.next

    return head


# ---------- Demo ----------
head = None
for v in [1, 6, 4, 8, 6, 4]:
    head = insert_sorted(head, v)

print("List after sorted insertions:")
print_list(head)  # Expect: 1, 4, 4, 6, 6, 8

head = delete_value(head, 4)
print("\nList after deleting FIRST 4:")
print_list(head)  # Expect: 1, 4, 6, 6, 8

head = delete_all(head, 6)
print("\nList after deleting ALL 6s:")
print_list(head)  # Expect: 1, 4, 8
