class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_loop_start(head):
    # Check if the linked list is empty or has only one node
    if not head or not head.next:
        return None

    slow = head
    fast = head

    # Move slow pointer by one and fast pointer by two
    slow = slow.next
    fast = fast.next.next

    # Find the meeting point of slow and fast pointers
    while fast and fast.next:
        if slow == fast:
            break
        slow = slow.next
        fast = fast.next.next

    # If the loop is not found, return None
    if slow != fast:
        return None

    # Move slow pointer back to the head
    slow = head

    # Move slow and fast pointers at the same speed until they meet again
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Return the starting point of the loop
    return slow


# Create a linked list with a loop
node1 = Node(3)
node2 = Node(2)
node3 = Node(0)
node4 = Node(-4)

head = node1
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Create the loop

# Call the function to detect the starting point of the loop
loop_start = detect_loop_start(head)

# Find the index of the loop start node
index = 0
current = head
while current != loop_start:
    current = current.next
    index += 1

# Print the output
print("Tail connects to node index", index)
