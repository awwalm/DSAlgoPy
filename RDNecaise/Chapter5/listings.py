
# Listing 5.1 Implementation of the linear search on an unsorted sequence.
def linearSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        # If the tsrget is in the ith element, return True
        if theValues[i] == target:
            return True
    return False    # If not found, return False

# Listing 5.2 Implementation of the linear search on a sorted sequence.
def sortedLinearSearch(theValues, item):
    n = len(theValues)
    for i in range(n):
        # If the tsrget is in the ith element, return True
        if theValues[i] == item:
            return True
        elif theValues[i] > item:
            return False
    return False

# Listing 5.3 Searching for the smallest value in an unsorted sequence.
def findSmallest(theValues):
    n = len(theValues)
    # Assume the first item is the smallest value.
    smallest = theValues[0]
    # Determine if any other item in the sequence s smaller
    for i in range(1, n):
        if theValues[i] < smallest:
            smallest = theValues[i]
    return smallest

# Listing 5.4 Implementation of the binary search algorithm.
# noinspection PyUnusedLocal
def binarySearch(theValues, target):
    # Start with the entire sequence of elements.
    low = 0
    high = len(theValues) - 1

    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high:
        # Find the midpoint of the sequence.
        mid = (high + low) // 2
        # Does the midpoint contain the target?
        if theValues[mid] == target:
            return True
        # Or does the target precede the midpoint?
        elif target < theValues[mid]:
            high = mid - 1
        # Or does it follow the midpoint?
        else:
            low = mid + 1
        return False

# Listing 5.5 Implementation of the bubble sort algorithm.
def bubbleSort(theSeq):
    """Sorts a sequence in ascending order using the bubble sort algorithm."""
    n = len(theSeq)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1):
        # Bubble the largest item to the end
        for j in range(n - 1):
            if theSeq[j] > theSeq[j + 1]:       # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp

# Listing 5.6 Implementation of the selection sort algorithm.
def selectionSort(theSeq):
    n= len(theSeq)
    for i in range(n - 1):
        # Assume the ith element is the smallest
        smalNdx = i
        # Determine if any other element contains a smaller value
        for j in range(i + 1, n):
            if theSeq[j] < theSeq[smalNdx]:
                smalNdx = j
        # Swap the ith value and smallNdx value only if the smallest value is
        # not already in its proper position. Some implementations omit testing
        # the condition and always swap the two values.
        if smalNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smalNdx]
            theSeq[smalNdx] = tmp

# Listing 5.7 Implementation of the insertion sort algorithm.
def insertionSort(theSeq):
    """Sorts a sequence in ascending order using the insertion sort algorithm"""
    n = len(theSeq)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positoned
        value = theSeq[i]
        # Find the position where value fits in the ordered part of the list
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            # Shift the items to the right during the search.
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        # Put the saved value into the open slot.
        theSeq[pos] = value

# Listing 5.8 Finding the location of a target value using the binary search.
def findSortedPosition(theList, target):
    """Modified version of the binary search that returns the index within
    a sorted sequence indicating where the target should be located."""
    low = 0
    high = len(theList) - 1
    while low <= high:
        mid = (high + low) // 2
        if theList[mid] == target:
            return mid                  # Index of the target
        elif target < theList[mid]:
            high = mid - 1
        else:
            low = mid + 1

# Listing 5.9 Merging two sorted lists.
def mergeSortedLists(listA, listB):
    """Merges two sorted lists to create and return a new sorted list."""
    newList = list()
    a = 0
    b = 0

    # Merge the lists together until one is empty
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1

    # If listA contaiins more items, append them to newList
    while a < len(listA):
        newList.append(listA[a])
        a += 1

    # Or if listB contains more items, append them to newList
    while b < len(listB):
        newList.append(listB[b])
        b += 1

    return newList

s8 = [-15, -3, 0, 4, 15, 18, 25]  # [4,8,15,23,42]
s9 = [1, 3, 4, 5, 7, 9] # [1,2,3,4,5,6,7,8,9]
print("\nl1:\t\t\t\t\t", s8)
print("l2:\t\t\t\t\t", s9)
s10 = mergeSortedLists(s8, s9)
print("Merged l1 and l2:\t", s10)


s6 = [4,1,5,7,4,9,-3,3,-15,15,0,25,18]
insertionSort(s6)
print(s6)
