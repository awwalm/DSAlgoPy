"""Sorting (and search) algorithm snippets and variants - implemented from scratch.

+ Binary Search
+ Insertion Sort
+ Selection Sort
+ Bubble Sort
+ Quick Sort
+ Heap Sort
+ Merge Sort
+ Radix Sort
+ Bucket Sort
"""

import heapq
import math
import queue
from typing import Mapping, SupportsInt, Sequence


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
    if len(seq) < 2: return
    for i in range(1, len(seq)):
        j, k = i-1, i
        while j > -1:
            if seq[k] < seq[j]:
                seq[k], seq[j] = seq[j], seq[k]
            j -= 1
            k -= 1

s2 = [4,1,5,7,4,9,-3,3,-15,15,0,25,18]
print("Original Sequence:\t", s2, "\n")
insertion_sort(s2)
print("Insertion Sort:\t\t", s2)


def selection_sort_too_many_rewrites(seq):
    if len(seq) < 2: return
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[j] < seq[i]:
                seq[i], seq[j] = seq[j], seq[i]

def selection_sort(seq):
    if len(seq) < 2: return
    for i in range(len(seq)):
        minval, searchpos = seq[i], i
        for j in range(i+1, len(seq)):
            if seq[j] < minval:
                minval, searchpos = seq[j], j
        seq[i], seq[searchpos] = minval, seq[i]

s3 = [4,1,5,7,4,9,-3,3,-15,15,0,25,18]
selection_sort(s3)
print("Selection Sort:\t\t", s3)


def bubble_sort_too_many_passes(seq):
    if len(seq) < 2: return
    for i in range(len(seq)):
        for j in range(1, len(seq)):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]

def bubble_sort(seq):
    k = len(seq)
    if k < 2: return
    while k > 0:
        for i in range(1, k):
            if seq[i] < seq[i-1]:
                seq[i], seq[i-1] = seq[i-1], seq[i]
        k -= 1

s4 = [4,1,5,7,4,9,-3,3,-15,15,0,25,18]
bubble_sort(s4)
print("Bubble Sort:\t\t", s4)


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


def inbuilt_heapsort(seq):
    n = len(seq)
    heapq.heapify(seq)
    for i in range(n): yield heapq.heappop(seq)

s7 = [4,1,5,7,4,9,-3,3,-15,15,0,25,18]
s7 = list(inbuilt_heapsort(s7))
print("Heap-Sort:\t\t\t", s7)


def merge_sorted_lists(l1, l2):
    len1, len2 = len(l1), len(l2)
    i1, i2, M = 0, 0, []                # Index variables for l1 and l2, M = merged container

    while (i1 < len1) and (i2 < len2):  # Merge items in order until at LEAST one list is empty
        if l1[i1] < l2[i2]:
            M.append(l1[i1])
            i1 += 1
        else:  # if l1[i1] > l2[i2]:
            M.append(l2[i2])
            i2 += 1

    while i1 < len1:                    # If l1 is not empty, copy over remaining items
        M.append(l1[i1])
        i1 += 1

    while i2 < len2:                    # If l2 is not empty, copy over remaining items
        M.append(l2[i2])
        i2 += 1

    return M                            # Return merged list

def merge_sort(seq):
    n = len(seq)
    if n < 2:
        return seq
    else:
        R = merge_sort(seq[n//2:])      # Right subsequence
        L = merge_sort(seq[:n//2])      # Left subsequence
        M = merge_sorted_lists(L, R)    # Merged subsequence
        return M

s5 = [4,1,5,7,4,9,-3,3,-15,15,0,25,18]
s5 = merge_sort(s5)
print("Merge-Sort:\t\t\t", s5)


def radix_sort_routine(seq):
    n = len(seq)
    if n < 2: return seq
    highest = max(seq)
    digits = 0
    while abs(highest) >= 10**digits: digits += 1
    bins = [queue.Queue(maxsize=n) for _ in range(10)]

    power = 0
    for d in range(digits):
        for i in range(n):
            # Index for `bins` is determined by nth digit of an element in seq, from its RHS.
            # This is done incrementally (n-1th digit from the RHS is considered in second round)
            # for a total of rounds corresponding to the item with most digits.
            # This is done by dividing ALL items with incremental powers of 10 (from 0) per round,
            # and then obtaining the modulus of the quotient by 10.
            bins[ (seq[i] // 10**power) % 10 ].put(seq[i])

        ndx = 0
        for b in range(10):
            while not bins[b].empty():
                seq[ndx] = bins[b].get()
                ndx += 1
        power += 1

    return seq

def radix_sort(seq):
    negatives = radix_sort_routine([i for i in seq if i < 0])
    positives = radix_sort_routine([i for i in seq if i >= 0])
    return negatives + positives

s11 = [4,1,5,7,4,9,-3,3,-15,15,0,25,18]
s11 = radix_sort(s11)
print("Radix-Sort:\t\t\t", s11)


def bogo_bucket_sort(seq):  # Do not try this at home !!!
    def sort_buckets(_seq: list, capacity: int):
        n = len(_seq)
        bucket = [queue.Queue(maxsize=n) for _ in range(capacity + 1)]
        for k in _seq:
            bucket[k].put(k)
        _seq = []
        for b in bucket:
            while not b.empty():
                _seq.append(b.get())
        return _seq

    unsorted_negatives = [i for i in seq if i < 0]
    unsorted_positives = [i for i in seq if i >= 0]
    negatives = sort_buckets(unsorted_negatives, max([abs(i) for i in unsorted_negatives]))
    positives = sort_buckets(unsorted_positives, max(unsorted_positives))
    return negatives + positives

def bucket_sort(seq):
    n = len(seq)
    if n < 2: return
    lowest, highest = min(seq), max(seq)
    num_buckets = int(math.sqrt(highest - lowest)) # math.ceil((highest - lowest) / (n//2))
    buckets: Mapping[SupportsInt: Sequence] = { i: [] for i in range(num_buckets) }

    for i in range(n):
        # Bucket index calculates an offset (distance between current and lowest values)
        # divided by value range, in order to weigh it on a scale of [0.0, ..., 1.0].
        # We simply multiply this scale by number of buckets (minus 1, for index correction)
        # to scale it back to available indices range of [0, 1, ..., num_buckets-1].
        bucket_index = int((seq[i] - lowest) / (highest - lowest) * (num_buckets - 1))
        heapq.heappush(buckets[bucket_index], seq[i])

    for b in buckets: print(buckets[b])     # [Debugging purposes] Show all buckets

    j = 0
    for i in range(len(buckets)):
        while len(buckets[i]) > 0:
            seq[j] = heapq.heappop(buckets[i])
            j += 1

s12 = [4,1,5,7,4,9,-3,3,-15,15,0,25,18]
#bucket_sort(s12)
# print("Bucket-Sort:\t\t", s12)
A = [10,51,2,18,4,31,13,5,23,64,29]
B = [4,8,15,16,23,42]
C = [23,34,78,-1,6,90,343,5]
D = [1,5,18,5,6,1,20]
for s in s12,A,B,C,D :
    bucket_sort(s)
    print("Bucket-Sort:\t\t", s, "\n")


s8 = [-15, -3, 0, 4, 15, 18, 25]  # [4,8,15,23,42]
s9 = [1, 3, 4, 5, 7, 9] # [1,2,3,4,5,6,7,8,9]
print("\nl1:\t\t\t\t\t", s8)
print("l2:\t\t\t\t\t", s9)
s10 = merge_sorted_lists(s8, s9)
print("Merged l1 and l2:\t", s10)
