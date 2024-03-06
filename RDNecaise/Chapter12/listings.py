from RDNecaise.Chapter5.listings import mergeSortedLists as mergeOrderedLists

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
