"""Provides a variety of data structures and abstract data types."""

__author__ = "Sam J. Griffiths"

import time


# LISTS, STACKS AND QUEUES

class SinglyLinkedNode:
    """Singly-linked list node.

    Attributes:
        value: Value stored in node.
        next: Reference to next node, or None if tail node.

    """

    def __init__(self, value=None, next=None):
        """Construct a SinglyLinkedNode.

        Args:
            value (optional): Value stored in node. Defaults to None.
            next (optional): Reference to next node. Defaults to None.

        """
        self.value = value
        self.next = next


def make_singly_linked_list(*args):
    """Make a singly-linked list containing the given arguments.

    Returns:
        SinglyLinkedNode: Head of linked list.

    """
    # If no arguments are given, return None
    if len(args) == 0:
        return None

    # If at least one argument is given, make a list
    head = SinglyLinkedNode(args[0])
    node = head
    for arg in args[1:]:
        node.next = SinglyLinkedNode(arg)
        node = node.next

    return head


def linked_list_print(head):
    """Print all values in a linked list.

    Args:
        head: First node in linked list.

    """
    node = head
    while node is not None:
        print(node.value, end=" ")
        node = node.next
    print()


def linked_list_search(head, value):
    """Query if a value is in a linked list.

    Args:
        head: First node in linked list.
        value: Value to query presence of.

    Returns:
        True if value is in list, False otherwise.

    """
    node = head
    while node is not None:
        if node.value == value:
            return True
        else:
            node = node.next

    return False


def linked_list_insert_front(head, value):
    """Insert a value at the front of a linked list.

    Args:
        head: First node in linked list.
        value: Value to insert.

    Returns:
        SinglyLinkedNode: New head of list.

    """
    return SinglyLinkedNode(value, head)


def linked_list_insert_back(head, value):
    """Insert a value at the back of a linked list.

    Args:
        head: First node in linked list.
        value: Value to insert.

    Returns:
        SinglyLinkedNode: New head of list.

    """
    if head is None:
        return SinglyLinkedNode(value, head)

    node = head
    while node.next is not None:
        node = node.next
    node.next = SinglyLinkedNode(value)

    return head


class SinglyLinkedList:
    """Singly-linked list of values.

    Attributes:
        head: First node in linked list.

    """

    def __init__(self, *args):
        """Construct a SinglyLinkedList containing the given arguments."""
        self.head = make_singly_linked_list(*args)

    def __str__(self):
        """Provide string representation for print() etc.

        Returns:
            str: String representation.

        """
        result = ""
        node = self.head
        while node is not None:
            result += str(node.value) + " "
            node = node.next
        return result

    def __len__(self):
        """Provide length of list for len() etc.

        Returns:
            int: Length of list.

        """
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def __contains__(self, value):
        """Query if a value is in the list for 'in' etc.

        Args:
            value: Value to query presence of.

        Returns:
            bool: True if value is in list, False otherwise.

        """
        return linked_list_search(self.head, value)

    def front(self):
        """Return the value at the front of the list.

        Returns:
            First value in list.

        """
        if self.head is None:
            raise IndexError("front of empty list")

        return self.head.value

    def back(self):
        """Return the value at the back of the list.

        Returns:
            Last value in list.

        """
        if self.head is None:
            raise IndexError("back of empty list")

        # Get last node -- tail reference would be quicker here!
        node = self.head
        while node.next is not None:
            node = node.next

        return node.value

    def insert_front(self, value):
        """Insert a value at the front of the list.

        Args:
            value: Value to insert.

        """
        self.head = linked_list_insert_front(self.head, value)

    def insert_back(self, value):
        """Insert a value at the back of the list.

        Args:
            value: Value to insert.

        """
        self.head = linked_list_insert_back(self.head, value)

    def remove_front(self):
        """Remove the value at the front of the list."""
        if self.head is None:
            raise IndexError("remove_front from empty list")

        self.head = self.head.next

    def remove_back(self):
        """Remove the value at the back of the list."""
        if self.head is None:
            raise IndexError("remove_back from empty list")

        if self.head.next is None:
            self.head = None
        else:
            # Get penultimate node -- doubly-linked would be quicker here!
            penultimate = self.head
            while penultimate.next.next is not None:
                penultimate = penultimate.next
            penultimate.next = None


class Stack:
    """Stack of values in a last-in, first-out (LIFO) basis."""

    def __init__(self):
        """Construct an empty Stack."""
        self._data = SinglyLinkedList()

    def push(self, value):
        """Insert a value onto the top of the stack.

        Args:
            value: Value to push.

        """
        self._data.insert_front(value)

    def pop(self):
        """Return and remove the value on the top of the stack.

        Returns:
            Value on top of stack.

        """
        value = self._data.front()
        self._data.remove_front()
        return value

    def empty(self):
        """Determine if the stack is empty, i.e. has no elements.

        Returns:
            True if stack is empty, False otherwise.

        """
        return len(self._data) == 0


class Queue:
    """Queue of values in a first-in, first-out (FIFO) basis."""

    def __init__(self):
        """Construct an empty Queue."""
        self._data = SinglyLinkedList()

    def push(self, value):
        """Insert a value onto the back of the queue.

        Args:
            value: Value to push.

        """
        self._data.insert_back(value)

    def pop(self):
        """Return and remove the value on the front of the queue.

        Returns:
            Value on front of queue.

        """
        value = self._data.front()
        self._data.remove_front()
        return value

    def empty(self):
        """Determine if the queue is empty, i.e. has no elements.

        Returns:
            True if queue is empty, False otherwise.

        """
        return len(self._data) == 0
