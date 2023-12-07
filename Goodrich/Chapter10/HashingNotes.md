
# Understanding Bitwise Operations and Hashing

## Introduction

In the realm of computer science and low-level programming, bitwise operations play a crucial role in data manipulation, encoding, and hashing. This note explores fundamental concepts such as bitwise AND, OR, XOR operations, as well as the application of these operations in hash functions. Examples and explanations are provided to enhance understanding.

## Bitwise Operations

### AND Operation

The bitwise AND operation (`&`) is a binary operation that results in a 1 only if both corresponding bits are 1. It is often used for masking and isolating specific bits. The truth table is as follows:

```plaintext
| A | B | A & B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   0   |
| 1 | 0 |   0   |
| 1 | 1 |   1   |
```

#### Example:

```python
result = 0b1101 & 0b1010  # Result: 0b1000
```

### OR Operation

The bitwise OR operation (`|`) results in a 1 if at least one of the corresponding bits is 1. It is commonly used for setting or adding specific bits.

```plaintext
| A | B | A | B |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 |
```

#### Example:

```python
result = 0b1101 | 0b1010  # Result: 0b1111
```

### XOR Operation

The XOR operation (`^`) results in a 1 if the corresponding bits are different. It is often used for toggling or flipping specific bits.

```plaintext
| A | B | A ^ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   0   |
```

#### Example:

```python
result = 0b1101 ^ 0b1010  # Result: 0b0111
```

## Hashing with Bitwise Operations

Hash functions are essential in computer science, and bitwise operations can be employed to create simple hash functions. Below is an example Python code for a basic hash function:

```python
def hash_code(s):
    mask = (1 << 32) - 1
    h = 0
    for character in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(character)
    return h

# Example
hashed_value = hash_code("hello")
print(f"Hashed Value: {hashed_value}")
```

#### Explanation:

1. **Initialization:**
   ```python
   mask = (1 << 32) - 1
   h = 0
   ```
   - `mask` is a 32-bit mask.
   - `h` is initialized to 0.

2. **Iterating Over Characters in "hello":**
   ```python
   for character in "hello":
        h = (h << 5 & mask) | (h >> 27)
        h += ord(character)
   ```
   - The hash value `h` is updated using bitwise operations and the ASCII value of each character.

3. **Final Result:**
   ```python
   print(f"Hashed Value: {hashed_value}")
   ```
   - The final hash value for the string "hello" is printed.

## Compression Functions

### Premise
In the event that two distinct keys map to the same value (see [Collision](#collision)), 
we introduce a **bucket array** to mediate this whereby each bucket may manage a collection
of items that are sent to a specific index by the hash function.

### Definition
Let $`A`$ be a bucket array of size $`N`$ containing $`n`$ elements. 
We define a **hash function** $`h(k)`$ where $`k`$ is a key as follows:
```math
\begin{align*}
   h(k) \rightarrow i, \exists i \in [0,N-1], \forall i \in \mathbb{N}
\end{align*}
```
The value of $`h(k)`$ is strictly an index that can be queried by $`A[h(k)=i]`$.

### Collision
When $`h(k)`$ and $`h({k}')`$ both map to the same value $`v`$, it indicates a collision.

### Hash Coding & Compression
The 1st stage of hashing consists of **hash coding**, this entails mapping a key to an arbitray integer.
The 2nd stage, known as **compression**, involves transformation of that hashcode to an integer
limited to a range within the bucket $`A`$.

### Polynomial Hashcodes
Simply taking the Unicode values of characters during hash coding (see [Bitwise Hashing](#hashing-with-bitwise-operations))
is not enough as it opens the floodgates to collision. Thusly, we derive a polynomial $`h(x)`$ 
for the characters of a string delineated by the tuple $`( x_0 , x_1, x_2, \ldots, x_{n-1} )`$ as

```math
\begin{align*}
   h(x) := x_{0}a^{n-1} + x_{1}a^{n-2} + \ldots + x_{n-2}a^{1} + x_{n-1}a^{0}
\end{align*}
```
By Horner's law, $`h(x)`$ can be further simplified as follows:
```math
\begin{align*}
   h(x) := x_{n-1} + a(x_{n-2} + a(x_{n-3} + \ldots + a(x_{2} + a(x_{1} + ax_{0})) \ldots ))
\end{align*}
```

## Efficiency of Hash Tables

<table>
    <thead>
        <tr>
            <th rowspan=2>Operation</th>
            <th rowspan=2">List</th>
            <th colspan="2">Hash Table</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan=2></td>
            <td>Expected</td>
            <td>Worst Case</td>
        </tr>
        <tr>
            <td><code>__getitem__</code></td>
            <td>O(n)</td>
            <td>O(1)</td>
            <td>O(n)</td>
        </tr>
        <tr>
            <td><code>__setitem__</code></td>
            <td>O(n)</td>
            <td>O(1)</td>
            <td>O(n)</td>
        </tr>
        <tr>
            <td><code>__delitem__</code></td>
            <td>O(n)</td>
            <td>O(1)</td>
            <td>O(n)</td>
        </tr>
        <tr>
            <td><code>__len__</code></td>
            <td>O(1)</td>
            <td>O(1)</td>
            <td>O(1)</td>
        </tr>
        <tr>
            <td><code>__iter__</code></td>
            <td>O(n)</td>
            <td>O(n)</td>
            <td>O(n)</td>
        </tr>
    </tbody>
</table>

Comparison of the running times of the methods of a map realized by means of an unsorted list or a hash table. 
We let n denote the number of items in the map, and we assume that the bucket array supporting the hash table 
is maintained such that its capacity is proportional to the number of items in the map.

## Exercises (more [here](./Exercises))

- R-10.6 Which of the hash table collision-handling scheme(s) (CHS) could tolerate a load factor above 1 and which could not?
> We know that a lookup table having a load factor $`n/N`$ works best when kept to 1. If it exceeds this threshold,
a bucket array with *separate-chaining* CHS could keep functioning with acceptable performance.
An explicit storage lookup table on the other hand would have to resize every single time 
as there are no buckets to handle a total number of items exceeding the length of the lookup table itself.

- R-10.8 What would be a good hash code for a vehicle identification number that is a string of numbers 
and letters of the form “9X9XX99X9XX999999,” where a “9” represents a digit and an “X” represents a letter?
> We want to avoid XOR and OR operations on the bit values since there are repititive patterns.
Polynomial hashcodes are suitable.

- R-10.13 What is the worst-case time for putting n entries in an initially empty hash table, 
with collisions resolved by chaining? What is the best case?
> If the size of the table is n, the runtime is quadratic because 1 op is performed for first item,
then 2 ops for second item, ..., then n ops for the nth item. This is due to prevention of duplicate keys.
If there are certainly no duplicates, linear runtime is possible.

- R-10.18 Explain why a hash table is not suited to implement a sorted map.
> For the hash function (and *especially* the compression function) to be consistent,
a leap of faith is required to let it determine the index it chooses for a value of a hashed key.
Since the hash function is the index governor, sorting becomes unreasonable.

- R-10.19 Describe how a sorted list implemented as a doubly linked list 
could be used to implement the sorted map ADT.
> Since no hashing is involved, simply determine the ranking criteria immediately before insertion.

- R-10.20 What is the worst-case asymptotic running time for performing n deletions 
from a [`SortedTableMap`](./sorted_table_map.py) instance that initially contains 2n entries?
> **Here's the breakdown, given a sorted table map $`M`$**:
> 
> - Deletion calls the binary search method to attempt to locate the items first.
> - Once located, deletion results in reconstructing a portion of the array.
> - This leads to a threshold of $`O(n)`$ time for each delete.
> - Hence, the runtime for deleting n items is $`\theta(\sum_{i}^{j}\lvert n \rvert) \medspace \exists n \in M`$.
