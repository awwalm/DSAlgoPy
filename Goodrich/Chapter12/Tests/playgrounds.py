"""Sample snippets and short tests."""

def bin_search(val, seq, start, end):
    if end < start:      # if start == len(seq) or end == 0     # Range exceeded
        return False
    else:
        mid = (start + end) // 2
        if val == seq[mid]:
            return True
        elif val < seq[mid]:
            return bin_search(val, seq, start, mid-1)
        else:                                                   # val > seq[mid]
            return bin_search(val, seq, mid+1, end)

s = [-15,2,3,4,5,6,7,8]
print(f"-9 in {s}: {bin_search(-9, s, 0, len(s)-1)}")      # False
print(f"7 in {s}: {bin_search(7, s, 0, len(s)-1)}\n")    # True

def insertion_sort(seq):
    if 0 <= len(seq) <= 1: return
    for i in range(1, len(seq)):
        j, k = i-1, i
        while j > -1:
            if seq[k] < seq[j]:
                seq[k], seq[j] = seq[j], seq[k]
            j -= 1
            k -= 1

s2 = [4,1,5,7,4,9,-3,3,-15,15,0,25,18]
print("Original Sequence:\t", s2)
insertion_sort(s2)
print("Insertion Sort:\t\t", s2)

def selection_sort_too_many_rewrites(seq):
    if 0 <= len(seq) <= 1: return
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[j] < seq[i]:
                seq[i], seq[j] = seq[j], seq[i]

def selection_sort(seq):
    if 0 <= len(seq) <= 1: return
    for i in range(len(seq)):
        minval, searchpos = seq[i], i
        for j in range(i+1, len(seq)):
            if seq[j] < minval:
                minval, searchpos = seq[j], j
        seq[i], seq[searchpos] = minval, seq[i]

s3 = [4,1,5,7,4,9,-3,3,-15,15,0,25,18]
selection_sort(s3)
print("Selection Sort:\t\t", s3)

def bubble_sort(seq):
    if 0 <= len(seq) <= 1: return
    for i in range(len(seq)):
        for j in range(1, len(seq)):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]

s4 = [4,1,5,7,4,9,-3,3,-15,15,0,25,18]
bubble_sort(s4)
print("Bubble Sort:\t\t", s4)

def merge_sort(seq):
    if len(seq) == 0: return seq
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]
    if len(seq) > 1:
        merge_sort(left)
        merge_sort(right)
    lsize, rsize = mid, len(seq) - mid
    i, l, r = 0, 0, 0
    while l < lsize and r < rsize:
        if left[l] < right[r]:
            seq[i] = left[l]
            i += 1
            l += 1
        else:
            seq[i] = right[r]
            i += 1
            r += 1
    while l < lsize:
        seq[i] = left[l]
        i += 1
        l += 1
    while r < rsize:
        seq[i] = right[r]
        i += 1
        r += 1

s5 = [4,1,5,7,4,9,-3,3,-15,15,0,25,18]
merge_sort(s5)
print("Merge-Sort:\t\t\t", s5)

def quick_sort(seq, start, end):
    if len(seq) < 2 or start >= end:            # Sequence/subsequence with 1 or 0 items is already sorted
        return
    pivot = partition(seq, start, end)          # Obtain pivot position
    quick_sort(seq, start, pivot)               # Recursively sort LEFT subsequence
    quick_sort(seq, pivot+1, end)               # Recursively sort RIGHT subsequence

def partition(seq, i, j):
    p = i                                       # Set first item as pivot
    while i < j:
        while seq[i] <= seq[p] and i < j:       # From START, find element seq[i] greater than pivot (seq[p])
            i += 1
        while seq[j] >= seq[p]:                 # From END, find element seq[j] less than pivot (seq[p])
            if j < i: break
            j -= 1
        if i < j:                               # Ensure range is still valid before outer while loop can verify
            seq[i], seq[j] = seq[j], seq[i]     # Once found, place greater element to the right, and less to left
    if j <= i: seq[p], seq[j] = seq[j], seq[p]  # Set pivot element in correct place (always with j)
    p = j                                       # Update pivot location
    return p                                    # Return pivot position to caller (quick sort)

s6 = [4,1,5,7,4,9,-3,3,-15,15,0,25,18]
quick_sort(s6, 0, len(s6)-1)
print("Quick-Sort:\t\t\t", s6)
