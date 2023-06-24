"""Code Fragment 7.14/.15/.16: A ``PositionalList`` class based on a doubly linked list."""
from __future__ import annotations
from overrides import override
from doubly_linked_list import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    # Nested Position class --------------------------------------------------------------------
    class Position:
        """An abstraction representing the location of a single element."""
        def __init__(self, container: PositionalList, node: _DoublyLinkedBase._Node):
            """Constructor should not be invoked by user.\n
            :param container: The parent of the ``_Node`` described by this ``Position`` object.
            :param node: A ``_Node`` object described by the calling ``Position``."""
            self._container = container
            self._node = node

        @property
        def __container(self):
            return self._container

        @property
        def __node(self):
            return self._node

        def element(self):
            """Return the element stored at this ``Position``."""
            return self._node.__element

        def __eq__(self, other: PositionalList.Position):
            """Return ``True`` if other is a ``Position`` representing the same location."""
            return type(other) is type(self) and other.__node is self._node

        def __ne__(self, other):
            """Return ``True`` if other does not represent the same location."""
            return not (self == other)

    # Utility methods ---------------------------------------------------------------------------
    def _validate(self, p: Position):
        """:returns: Position p's node.
        :raises ValueError | TypeError: if p is not a Position object or belongs to other container."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p.__container is not self:
            raise ValueError("p does not belong to this container")
        if p.__node.__next is None:
            raise ValueError("p is no longer valid")                    # RIP bro, you'll be missed.
        return p.__node

    def _make_position(self, node: _DoublyLinkedBase._Node):
        """Return ``Position`` instance for a given ``node`` (or ``None`` if sentinel)."""
        if node is self._header or node is self._trailer:               # Boundary violation.
            return None
        else:
            return self.Position(self, node)                            # Legitimate position.

    # Accessors --------------------------------------------------------------------------------
    def first(self):
        """Return the first ``Position`` in the list (or ``None`` if the list is empty)."""
        return self._make_position(self._header.__next)

    def last(self):
        """Return the last ``Position`` in the list (or ``None`` if the list is empty)."""
        return self._make_position(self._trailer.__prev)

    def before(self, p: Position):
        """Return the ``Position`` just before Position ``p`` (or ``None`` if p is first)."""
        node = self._validate(p)                                        # Crash the program if invalid.
        return self._make_position(node.__prev)

    def after(self, p: Position):
        """Return the ``Position`` just after Position ``p`` (or ``None`` if p is last)."""
        node = self._validate(p)
        return self._make_position(node.__next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()                                      # Generator.
            cursor = self.after(cursor)

    # Mutators --------------------------------------------------------------------------------
    @override  # Override inherited  version Position, rather than Node.
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new ``Position``."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element ``e`` at the front of the list and return new ``Position``."""
        return self._insert_between(e, self._header, self._header.__next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new ``Position``."""
        return self._insert_between(e, self._trailer.__prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before ``Position p`` and return new ``Position``."""
        original = self._validate(p)
        return self._insert_between(e, original.__prev, original)

    def add_after(self, p, e):
        """Insert element e into list after ``Position p`` and return new `Position``."""
        original = self._validate(p)
        return self._insert_between(e, original, original.__next)

    def delete(self, p):
        """Remove and return the element at Position ``p``."""
        original = self._validate(p)
        return self._delete_node(original)                              # Inherited method returns element

    def replace(self, p, e):
        """Replace the element at ``Position p`` with ``e``.\n
        :return: the element formerly at Position p."""
        original = self._validate(p)
        old_value = original.__element                                  # Temporarily store old element.
        original.__element = e                                          # Replace with new element.
        return old_value                                                # Return the old element value.
