"""Code Fragment 6.2: Implementing a stack using a Python list as storage."""


class EmptyError(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Creates an empty stack."""
        self._data = []                                    # Nonpublic list instance.

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return ``True`` if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element ``e`` to the top of the stack."""
        self._data.append(e)                                # New item stored at end of list.

    def top(self):
        """Return (but do not remove) the element at the top of the stack.\n
        :raises EmptyError: if the stack is empty.
        """
        if self.is_empty():
            raise EmptyError("Stack is empty")
        return self._data[-1]                               # The last item in the list.

    def pop(self):
        """Remove and return the element from the top of the stack.\n
        :raises EmptyError: if the stack is empty.
        """
        if self.is_empty():
            raise EmptyError("Stack is empty")
        return self._data.pop()                             # Remove last item from list.
