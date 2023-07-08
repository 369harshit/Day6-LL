# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Function to detect a cycle in a linked list using
# Floyd’s cycle detection algorithm
def detectCycle(head):
    # take two references – `slow` and `fast`
    slow = fast = head

    while fast and fast.next:

        # move slow by one
        slow = slow.next

        # move fast by two
        fast = fast.next.next

        # if they meet any node, the linked list contains a cycle
        if slow == fast:
            return True

    # we reach here if slow and fast do not meet
    return False


if __name__ == '__main__':

    head = None
    for i in reversed(range(5)):
        head = Node(i + 1, head)

    # insert cycle
    head.next.next.next.next.next = head.next.next
    if detectCycle(head):
        print('Cycle Found')
    else:
        print('No Cycle Found')
