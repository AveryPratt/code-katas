"""Contains a script to evaluate the completion of pairs of
opening and closing parenthesis in a string."""


def get_parenthetics_status(input_string):
    """Returns a number determining the status of open/closed paranthesis
    in a string (1 for open, 0 for closed, -1 for broken)."""
    stack = Stack()
    for char in input_string:
        if char == ")" or char == "(":
            stack.push(char)
    count = 0
    while stack.head is not None:
        if count < 0:
            return -1
        val = stack.pop()
        if val == "(":
            count += 1
        else:
            count -= 1
    if count == 0:
        return 0
    else:
        return 1


class Stack(object):
    """Basic last-in/first-out data structure.

    push: adds an item to the stack.
    pop: removes one item from the top of the stack."""
    def __init__(self):
        """Creates an empty stack (using only the 'self' parameter)."""
        self.head = None

    def push(self, val):
        """Creates a node containing the input value and adds it to the head of the stack."""
        self.head = Node(val, self.head)

    def pop(self):
        """Removes the node at the head of the stack, replacing it with the next node,
        and returns the value of the removed node."""
        val = self.head.val
        self.head = self.head.next_node
        return val


class Node(object):
    """A container for values being added to a singly-linked data structure."""
    def __init__(self, val, next_node):
        """Instatiates a new node containing the input value and is
        linked to the node given by the argument 'next_node'."""
        self.val = val
        self.next_node = next_node
