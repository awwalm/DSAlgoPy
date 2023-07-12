"""A proper circular singly linked list that inherits from ``SinglyLinkedList``."""
from Goodrich.Chapter7.Exercises.Utility.proper_singly_linked_list import SinglyLinkedList, EmptyError


class CircularSinglyLinkedList(SinglyLinkedList):
    """A class providing a circular singly linked list representation."""

    # Nested _Node class -----------------------------------------------------------------
    class _Node(SinglyLinkedList._Node):
        """Lightweight, nonpublic class for storing a circular singly linked node."""
        def __init__(self, element, next):
            super(CircularSinglyLinkedList._Node, self).__init__(element, next)

    # DoublyLinkedList methods ------------------------------------------------------------
    def __init__(self, head_element):
        super(CircularSinglyLinkedList, self).__init__(head_element)
        self._header._next = self._header                       # Circularity (node is both head and tail).

    def insert_before(self, e, guide: _Node):
        """Insert element ``e`` before a ``guide`` node and return new node."""
        newest = self._Node(e, guide)                           # Pre-linked before guide node.
        cur = self._header
        inserted = False
        if self.is_empty():                                     # If Linked List is empty, raise an exception.
            raise EmptyError("Linked List is empty")
        elif self._size == 1 or guide == self._header:          # If Linked List has singleton node and guide is head...
            self._header = newest                               # Make new node the header, pointed next to old head.
            inserted = True
        else:                                                   # If more than one node detected...
            cur = cur.next
            while cur is not self._header:                      # While current node is not tail...
                if cur.next == guide:                           # If node ahead of current node is guide...
                    cur.next = newest                           # Point the node before guide next to a new node.
                    inserted = True
                    break                                       # Insertion complete, terminate loop.
                cur = cur.next                                  # If not, keep iterating till tail.
        if not inserted:
            raise ValueError(f"Node {guide} not in {self}")     # In case node is not found, raise an exception.
        self._size += 1
        return newest

    def insert_after(self, e, guide: _Node):
        """Insert element ``e`` after a ``guide`` node and return new node."""
        newest = self._Node(e, guide.next)                      # Pre-linked to next node after guide node.
        cur = self._header
        inserted = False
        if self.is_empty():                                     # If Linked List is empty, raise an exception.
            raise EmptyError("Linked List is empty")
        elif guide.next == self._header:                        # If this is the tail node.
            guide.next = newest                                 # Point guide next to new node.
            inserted = True
        else:                                                   # If one or more nodes detected...
            while cur.next is not self._header:                 # While-loop won't process tail node again!
                if cur == guide:                                # When guide node is found, mark insertion as done.
                    guide.next = newest                         # Point guide next to new node.
                    inserted = True
                    break
                cur = cur.next
        if not inserted:
            raise ValueError(f"Node {guide} not in {self}")     # In case node is not found, raise an exception.
        self._size += 1
        return newest

    def delete_node(self, node: _Node):
        """Delete node from the list and return its element."""
        cur = self._header                                      # Head node.
        element = node.element
        deleted = False
        if self.is_empty():                                     # If Linked List is empty, raise an exception.
            raise EmptyError("Linked List is empty")
        elif self._size == 1:                                   # If Linked List has singleton node...
            node.element = None                                 # Deprecate node (next pointer is not modified!).
            deleted = True
        elif node == self._header:                              # If node to be deleted is head node...
            cur = self._header.next                             # Shift cur ahead of head node inorder to traverse.
            while True:
                if cur.next == self._header:
                    cur.next = self._header.next
                    self._header.next = self._header.element = None
                    self._header = cur.next
                    deleted = True
                    break
                cur = cur.next
        elif node.next == self._header:                         # If node to be deleted is tail node...
            while cur is not node.next:
                if cur.next == node:
                    cur.next = node.next
                    node.element = node.next = None             # Deprecate node.
                    deleted = True
                    break
                cur = cur.next
        else:                                                   # If any other node...
            while cur.next is not self._header:                 # Tail is ommitted (already processed).
                if cur.next == node:                            # Head is ommitted (already processed).
                    cur.next = node.next
                    node.element = node.next = None
                    deleted = True
                    break
                cur = cur.next
        if not deleted:
            raise ValueError(f"Node {node} not in {self}")      # In case node is not found, raise an exception.
        self._size -= 1
        return element
