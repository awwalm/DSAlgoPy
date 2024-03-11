from RDNecaise.Chapter2.array import Array
from RDNecaise.Chapter5.listings import mergeSortedLists as mergeOrderedLists
from RDNecaise.Chapter8.llistqueue import Queue


# Listing 12.1 Implementation of the merge sort algorithm for use with Python lists.
def pythonMergeSort(theList):
    """Sorts a Python list in ascending order using the merge sort algorithm."""
    # Check the base case - the list contains a single item
    if len(theList) <= 1:
        return theList
    else:
        # Compute the midpoint
        mid = len(theList) // 2

        # Split the list and perform the recursive step
        leftHalf = pythonMergeSort(theList[:mid])
        rightHalf = pythonMergeSort(theList[mid:])

        # Merge the two ordered sublists
        newList = mergeOrderedLists(leftHalf, rightHalf)
        return newList


# Listing 12.3 Merging two ordered virtual sublists.
def mergeVirtualSeq(theSeq, left, right, end, tmpArray):
    """Merges the two sorted virtual subsequences: [left...right), [right...end)
    using the tmpArray for intermediate storage."""
    # Initialize two subsequence index variables, and one for resulting merged array
    a = left
    b = right
    m = 0

    # Merge the two sequences together until one is empty
    while a < right and b < end:
        if theSeq[a] < theSeq[b]:
            tmpArray[m] = theSeq[a]
            a += 1
        else:
            tmpArray[m] = theSeq[b]
            b += 1
        m += 1

    # If the left subsequence contains more items, append them to tmpArray
    while a < right:
        tmpArray[m] = theSeq[a]
        a += 1
        m += 1

    # Or if right subsequence contains more, append them to tmpArray
    while b < end:
        tmpArray[m] = theSeq[b]
        b += 1
        m += 1

    # copy the sorted subsequence back into the original sequence structure
    for i in range(end - left):
        theSeq[i+left] = tmpArray[i]


# Listing 12.2 Improved implementation of the merge sort algorithm.
def recMergeSort(theSeq, first, last, tmpArray):
    """Sorts a virtual subsequence in ascending order using merge sort."""
    # The elements that comprise the virtual subsequence are indicated
    # by the range [first...last]. tmpArray is temporary storage used in
    # the merging phase of the merge sort algorithm.

    # Check the base case: the virtual sequence contains a single item
    if first == last:
        return
    else:
        # Compute the mid-point
        mid = (first + last) // 2

        # Split the sequence and perform the recursive step
        recMergeSort(theSeq, first, mid, tmpArray)
        recMergeSort(theSeq, mid+1, last, tmpArray)

        # Merge the two ordered subsequences
        mergeVirtualSeq(theSeq, first, mid+1, last+1, tmpArray)


# Listing 12.6 Implementation of the radix sort using an array of queues.
def radixSort(intList, numDigits):
    """Create an array of queues to represent the bins."""
    binArray = Array(10)
    for k in range(10):
        binArray[k] = Queue()

    # The value of the current column
    column = 1

    # Iterate over the number of digits in the largest value
    for d in range(numDigits):

        # Distribute the keys across the 10 bins
        for key in intList:
            digit = (key // column) % 10
            binArray[digit].enqueue(key)

        # Gather the keys from the bins and place them back in intList
        i = 0
        for bin_ in binArray:
            while not bin_.isEmpty():
                intList[i] = bin_.dequeue()
                i += 1

        # Advance to the next column value
        column *= 10


def addToSortedList(newList, curNode):
    newList.tail.next, newList.tail = curNode, curNode
    return newList


def llistInsertionSort(origList):
    """
    Sorts a linked list using the technique of the insertion sort.
    A reference to the new ordered list is returned.
    """
    # Make sure the list contains at least one node
    if origList is None:
        return None

    # Iterate through the original list
    newList = None
    while origList is not None:

        # Assign a temp reference to the first node
        curNode = origList

        # Advance the original list reference to the next node
        origList = origList.next

        # Unlink the first node and inset into the new ordered list
        curNode.next = None
        newList = addToSortedList(newList, curNode)

    # Return the list reference of the new ordered list
    return newList


def _splitLinkedList(subList):
    """
    Splits a linked list at the midpoint to create two sublists.
    The head reference of the right sublist is returned. The left sublist
    is still referenced by the original head reference.
    """
    # Assign a reference to the first and second nodes in the list
    midPoint = subList
    curNode = midPoint.next

    # Iterate through the list until curNode falls off the end
    while curNode is not None:
        # Advance curNode to the next node
        curNode = curNode.next

        # If there are more nodes, advance curNode again and midPoint once
        if curNode is not None:
            midPoint = midPoint.next
            curNode = curNode.next

    # Set rightList as the head pointer to the right sublist
    rightList = midPoint.next
    # Unlink the right sublist from the left sublist
    midPoint.next = None
    # Return the right sublist head reference
    return rightList


class ListNode:
    def __init__(self, value):
        self.data = value
        self.next = None


def _mergeLinkedLists(subListA, subListB):
    """Merges two sorted linked list; returns head refeence for the new list."""
    # Create a dummy node and insert it at the front of the list
    newList = ListNode(None)
    newTail = newList

    # Append nodes to the new list until one list is empty
    while subListA is not None and subListB is not None:
        if subListA.data <= subListB.data:
            newTail.next = subListA
            subListA = subListB.next
        else:
            newTail.next = subListB
            subListB = subListB.next
        newTail = newTail.next
        newTail.next = None

    # If self list contains more terms, append them
    if subListA is not None:
        newTail.next = subListA
    else:
        newTail.next = subListB

    return newList.next

def llistMergeSort(theList):
    """Sorts a linked list using merge sort. A new head reference is returned."""

    # If the list is empty (base case), return None
    if theList is None:
        return None

    # Split the linked list into two sublists of equal size
    rightList = _splitLinkedList(theList)
    leftList = theList

    # Perform the same operation on the left half...
    leftList = llistMergeSort(leftList)

    # ...and the right half
    rightList = llistMergeSort(rightList)

    # Merge the two ordered sublists
    theList = _mergeLinkedLists(leftList, rightList)

    # Return the head pointer of the ordered sublist
    return theList



