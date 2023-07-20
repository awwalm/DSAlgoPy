"""Implements the ``Bag`` ADT using a singly linked list."""


class Bag:
    def __init__(self):
        """Constructs an empty bag."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Returns the number of items in the bag."""
        return self._size

    def __contains__(self, target):
        """Determine if an item is contained in the bag."""
        curNode: _BagListNode = self._head
        while curNode is not None and curNode.item != target:
            curNode = curNode.next
        return curNode is not None

    def add(self, item):
        """Adds a new item to the bag."""
        newNode = _BagListNode(item)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    def remove(self, item):
        """Removes an instance of the item from the bag."""
        preNode = None
        curNode = self._head
        while curNode is not None and curNode.item != item:
            preNode = curNode
            curNode = curNode.next
        assert curNode is not None, "The item must be in the bag"
        self._size -= 1
        if curNode is self._head:
            self._head = curNode.next
        else:
            preNode.next = curNode.next
        return curNode.item

    def __iter__(self):
        """Returns an iterator for traversing the list of items."""
        # curNode = self._head
        # while curNode is not None:
        #    yield curNode.item
        #    curNode = curNode.next
        return _BagIterator(self._head)


class _BagIterator:
    def __init__(self, listHead):
        """Defines a linked list iterator for the ``Bag`` ADT."""
        self._curNode: _BagListNode = listHead

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item


class _BagListNode(object):
    def __init__(self, item):
        """Defines a private storage class for creatng list nodes."""
        self.item = item
        self.next = None
