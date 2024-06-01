# Notes on [_Data Structures & Algorithms in Python_](
https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/1118290275)

### Supporting Material (Similar Repos, Solved Problems, Tools)

- [Charles Reid's DSA/ML Repo with Java Solutions](https://github.com/charlesreid1/java)
- [Jihoon Kim's Worked Solutions (Till Chapter 8)](https://github.com/jihoonerd/Data_Structures_and_Algorithms_in_Python)
- [William Cameron's Solutions (Till Chapter 6)](https://github.com/wdlcameron/Solutions-to-Data-Structures-and-Algorithms-in-Python)
- [$`\underline{\LaTeX}`$ Equation Editor by Codecogs](https://latex.codecogs.com/eqneditor/editor.php)
- [Eric Rowell's Big-O Cheatsheet](https://bigocheatsheet.com)
- [Plaintext Diagram Editor](https://www.planttext.com)
- Use `curl -o filename.extension "URL"` syntaxt to download a file to `pwd`

<hr>


# 1. Object-Oriented Programming

- **Design Pattern**:
A pattern provides a general template for a solution that can be applied in many situations. 
It describes the **main elements** of a solution in an abstract way that can be specialized 
for a specific problem at hand. It consists of a **name**, which identifies the pattern; 
a **context**, which describes the scenarios for which this pattern can be applied; 
a **template**, which describes how the pattern is applied; 
and a **result**, which describes and analyzes what the pattern produces.

- **Dictionaries and the `__slots__` Declaration**:
By default, Python represents each namespace with an instance of the built-in `dict` class
that maps identifying names in that scope to the associated objects. A dictionary requires
additional memory beyond raw data contained in it. We avoid this inefficiency caveat by 
representing instance namespaces as string sequences (technically a `tuple`) assigned to
a class-level member called `__slots__`.
Sublcasses whose parents declare `__slots__` must declare it too, however, only additional
instance members must be provided. 

<hr>


# 2. Linked-Lists

- **Implemening Stacks and Queues via Linked Lists**:
Each `_Node` object [^1],[^2] used in structuring the linked list is unaware if it's the head 
or tail node. Only the controller or linked list object knows the head and tail references.


- **The Positional List ADT**:
As useless as it seems (this assumption proves to be ultimately true as the ADT serves no 
unique purpose), this data structure is just a facility for inserting and removing at any location 
in a doubly linked list. It can be argued that the accessing of a specific node (which at this time
of writing) via a selected routine can be done in constant time, but I maintain the position 
that this is **NOT exactly** $`O(1)`$ time, however.

  >Consider continuously reassigning a node variable to the next node until 
   the correct one is detected. Is this any different from iterating until 
   arriving at an item $`O(m \leq n)`$ ? Or perhaps, do we approximate 
   this to "constant time instant retrieval" $`O(k \geq 1)`$ ?


- **Implementing _Proper_ Linked Lists**:

  - Most of the conceptual "linked list" programs (or classes) in the book are 
  private **base** classes. The use of a proper or standard (whichever term you prefer) 
  linked list implies two things: re-inventing the wheel (re-writing your own classes); 
  extending an abstraction over the base classes.
  
  - I've gone for a better and rigid approach - implementing the classes by reusing 
  the patterns and structures from the base classes provided in the book, starting with 
  the singly linked list, and then extending all other variants (doubly, circular, etc.) 
  cascadingly or non-sequentially as desired.
  
  - This comes with several challenges such as dealing with dichotomies of Python's
  more obscure inheritance syntax. Nothing that can't be handled by enforcing D.R.Y. principles 
  (so far) and coverage tests.

[^1]: See class/method: [`linked_queue.LinkedQueue._Node`](Goodrich/Chapter7/linked_queue.py)

[^2]: See class/method: [`linked_stack.LinkedStack._Node`](Goodrich/Chapter7/linked_stack.py)

<hr>


# 3. Maps, Hash Tables, and Skip Lists

## Understanding Bitwise Operations and Hashing

### Introduction

In the realm of computer science and low-level programming, bitwise operations 
play a crucial role in data manipulation, encoding, and hashing. This section 
explores fundamental concepts such as bitwise AND, OR, XOR operations, as well as 
the application of these operations in hash functions. 
Examples and explanations are provided to enhance understanding.

## Bitwise Operations

### AND Operation

The bitwise AND operation (`&`) is a binary operation that results in a 1 only if both 
corresponding bits are 1. It is often used for masking and isolating specific bits. 
The truth table is as follows:

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

The bitwise OR operation (`|`) results in a 1 if at least one of the corresponding bits is 1. 
It is commonly used for setting or adding specific bits.

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

The XOR operation (`^`) results in a 1 if the corresponding bits are different. 
It is often used for toggling or flipping specific bits.

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

Hash functions are essential in computer science, and bitwise operations can be employed 
to create simple hash functions. Below is an example Python code for a basic hash function:

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
        # noinspection PyUnresolvedReferences,PyUnboundLocalVariable
        h = (h << 5 & mask) | (h >> 27)
        h += ord(character)
   ```
   - The hash value `h` is updated using bitwise operations and the ASCII value of each character.

3. **Final Result:**
   ```python
    # noinspection PyUnresolvedReferences
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
The 1st stage of hashing consists of **hash coding**, this entails mapping a key 
to an arbitray integer. The 2nd stage, known as **compression**, involves transformation 
of that hashcode to an integer limited to a range within the bucket $`A`$.

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

Comparison of the running times of the methods of a map realized by means of 
an unsorted list or a hash table. We let n denote the number of items in the map, 
and we assume that the bucket array supporting the hash table is maintained such that 
its capacity is proportional to the number of items in the map.

## Exercises (more [here](Goodrich/Chapter10/Exercises))

- R-10.6 Which of the hash table collision-handling scheme(s) (CHS) could tolerate
a load factor above 1 and which could not?

> We know that a lookup table having a load factor $`n/N`$ works best when kept to 1. 
If it exceeds this threshold, a bucket array with *separate-chaining* CHS could keep 
functioning with acceptable performance. An explicit storage lookup table on the other hand 
would have to resize every single time as there are no buckets to handle a total number 
of items exceeding the length of the lookup table itself.

- R-10.8 What would be a good hash code for a vehicle identification number that is 
a string of numbers and letters of the form “9X9XX99X9XX999999,” where a “9” represents 
a digit and an “X” represents a letter?

> We want to avoid XOR and OR operations on the bit values since there are repititive patterns.
Polynomial hashcodes are suitable.

- R-10.13 What is the worst-case time for putting n entries in an initially empty hash table, 
with collisions resolved by chaining? What is the best case?
> If the size of the table is n, the runtime is quadratic because 1 op is performed
for first item, then 2 ops for second item, ..., then n ops for the nth item. 
This is due to prevention of duplicate keys. If there are certainly no duplicates, 
linear runtime is possible.

- R-10.18 Explain why a hash table is not suited to implement a sorted map.

> For the hash function (and *especially* the compression function) to be consistent,
a leap of faith is required to let it determine the index it chooses for a value of a hashed key.
Since the hash function is the index governor, sorting becomes unreasonable.

- R-10.19 Describe how a sorted list implemented as a doubly linked list 
could be used to implement the sorted map ADT.
- 
> Since no hashing is involved, simply determine the ranking criteria immediately before insertion.

- R-10.20 What is the worst-case asymptotic running time for performing n deletions 
from a [`SortedTableMap`](Goodrich/Chapter10/sorted_table_map.py) instance that initially
contains 2n entries?

> **Here's the breakdown, given a sorted table map $`M`$**:
> 
> - Deletion calls the binary search method to attempt to locate the items first.
> - Once located, deletion results in reconstructing a portion of the array.
> - This leads to a threshold of $`O(n)`$ time for each delete.
> - Hence, the runtime for deleting n items is $`\theta(\Sigma\stackrel{j}{i} \lvert n \rvert), \exists n \in M`$.

<hr>


# 4. Binary Search Trees

* An effective way to store maps/key-value items is by the means of a binary search tree.

* We define a **binary search tree** (or BST) $`T`$ with each position $`p`$ 
storing a key-value pair $`(k,v)`$ such that:
  * Keys stored in the left subtree of $`p`$ are less than $`k`$.
  * Keys stored in the right subtree of $`p`$ are greater than $`k`$.
  * The **predecessor** of $`p`$ is located at the rightmost position under the left subtree.
  * The **successor** of $`p`$ is located at the leftmost position under the right subtree.

* Take note that the intuition behind a binary search tree is governed by the **inorder traversal**.

* Let's take the following as our example binary search tree.
```text
                     44              
                     |
             _-------+-------_
             |               |
             17              88
           /    \          /    \
          8     32        65    97
               /        /   \   /
              28       54   82 93
               \            /
               29          76
                            \
                            80
```

* Computing the successor of a position in a binary search tree yields the immediate number
that is larger than the one stored in that position. The running time is bounded by the height, i.e. $`O(h)`$.
> **Algorithm** after(p): <br>
> &emsp; if right(p) is not None then _{successor is leftmost position in $`p`$'s right subtree}_ <br>
> &emsp; &emsp; walk = right(p) <br>
> &emsp; &emsp; while left(walk) is not None do <br>
> &emsp; &emsp; &emsp; &emsp; walk = left(walk) <br>
> &emsp; &emsp; return walk <br>
> &emsp; else: _{successor is the nearest ancestor having $`p`$ in its subtree}_ <br>
> &emsp; &emsp; walk = p <br>
> &emsp; &emsp; ancestor = parent(walk) <br>
> &emsp; &emsp; while ancestor is not None and walk == right(ancestor) do <br>
> &emsp; &emsp; &emsp; &emsp; walk = ancestor <br>
> &emsp; &emsp; &emsp; &emsp; ancestor = parent(walk) <br>
> &emsp; &emsp; return ancestor

* The summary of the algorithm above can be broken down into the following steps:
  * Suppose we are looking for the successor of 65 (which should be 76).
  * We walk **rightwards** (82) and then check the left of that (76) and only step when there are no left nodes.
  * But what if we're looking for what comes after 32? (which should be 54).
  * The algorithm first attempts to check the right and since there is none, it shifts to the next scope block.
  * Here, we progressively walk **upwards** ensuring the child node is located at the right of its parent.
  * Once it's no longer on the right, the current value is returned. This is all based on the logic of inorder traversal.


# 5. Text Processing

## Boyer-Moore String Matching Algorithm 

The Boyer-Moore algorithm uses various heuristic(s) to conduct an efficient string match
as opposed brute-forcing. The general idea is to determine an ideal number of characters
to skip when finding a substring (**_pattern_**) in a **_text_**. 
There are several variants utilizing different heuristics.

### Partial/Simplified Boyer-Moore Algorithm
- **Objective:**  
>When a mismatch occurs, look at the pattern at an earlier position for
the occurrence of the mismatched character, then attempt to align, else shift past
mismatched character by one step and then repeat.

- **Heuristics Required: _Last-Occurrence Table_**

- **Example 1:**
  - Let _T_ := _A B A C A B_
  - Then _LOT_ := 

    | $c$              | _A_ | _B_ | _C_ | _*_ |
    |------------------|-----|-----|-----|-----|
    | $\text{last}(c)$ | 4   | 5   | 3   | -1  |

- **Example 2:**
  - Let _T_ := _B A O B A B_
  - Then _LOT_ := 

    | $c$              | _B_ | _A_ | _O_ | _*_ |
    |------------------|-----|-----|-----|-----|
    | $\text{last}(c)$ | 5   | 4   | 2   | -1  |

- **Resources:**
    - Main Reference (_DSA by Goodrich, Tamassia, and Goldwasser_)

### Horspool Algorithm
<small>Honestly deserves its own section, but we're associating it with Boyer-Moore for now.</small>
- **Objective:**
>When a mismatch occurs, take into account the number of recently matched characters
and derive the number of steps to skip based on a possible recurrence of the
partially matched portion of the pattern from the text, in the pattern.

- **Heuristic Required: _Shift-Value Table_**
    - Construction Note ⚠: Indices are reversed; last character is ignored; 
    all other characters (i.e. wildcard) are assigned value of length pattern;
    last character, if re-encountered prior to last position in pattern, must be recorded;
    no repeated enumerations.
    - Matching Notes: In case of partial match, calculate SVT for most recent matched character; 
    in case of no partial match, calculate and shift by SVT value of mismatched character.

- **Example 1:**
  - Let _T_ := _B A O B A B_
  - Indexing := 
  
    | 5   | 4   | 3   | 2   | 1   | 0   |
    |-----|-----|-----|-----|-----|-----| 
    | _B_ | _A_ | _O_ | _B_ | _A_ | _B_ |

  - Then _SVT_ := 

    | _A_ | _B_ | _0_ | _*_ |
    |-----|-----|-----|-----|
    | 1   | 2   | 3   | 6   |


- **References/Resources** (covers heuristic constructions):
  - _Introduction to the Design and Analysis of Algorithms by Anany Levitin (Chapter 7)_
  - _"Horspool Algorithm" by Dr. H S Guru Prasad_ ([video](https://youtu.be/W4h6555g5qo))
  
### Boyer-Moore-Horspool Algorithm
- **Objective:**
> On par with Horspool Algorithm, this hybrid aims to adapt the partial matching 
technique with a "Bad-Match Table". When a mismatch occurs, we proceed just as with
Horspool algorithm, with the new heuristic dictating the number of skips.

- **Heuristic Required: _Bad-Match Table_**
  - ⚠ Construction Notes: Normal indexing; start by assigning length of pattern as values 
  for wildcard and last character (subsequent occurences of last character are ignored); 
  take last occurence of subsequent characters distinct from last character in pattern.  
  - ⚠ Matching Notes: In case of partial match, calculate BMT for most recent matched character;
  in case of no partial match, calculate and shift by BMT value of mismatched character.

- **Example 1:**
  - Let _T_ := _B A O B A B_
  - Indexing := 
  
    | 0   | 1   | 2   | 3   | 4   | 5   |
    |-----|-----|-----|-----|-----|-----| 
    | _B_ | _A_ | _O_ | _B_ | _A_ | _B_ |

  - Then _BMT_ := 

    | _A_ | _O_ | _B_ | _*_ |
    |-----|-----|-----|-----|
    | 4   | 2   | 6   | 6   |

  
- **References/Resources** (covers heuristic constructions):
  - _"Boyer-Moore Pattern-Matching Algorithm" (it is in fact a [video](https://youtu.be/4Oj_ESzSNCk) 
      on the Boyer-Moore-Horspool variant) by Prof. Bharathi Ramesh_

### Classic Boyer-Moore Algorithm
- **Objective:**
> Utilizes both a Shift-Value Table and a Good-Suffix Rule to determine the correct number of skips.
This is a very complicated algorithm and the 7th chapter of Anany Levitin's book 
is extremely and absolutely recommended for it, and mandatory for sound understanding.

- **Heuristics Required:**
  - Shift-Value Table (same as with [Horspool](#horspool-algorithm))
  
  - Good Suffix Table 
  <br>See [quote from Wikipedia](
  https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm#The_good-suffix_rule):
      
    >Suppose for a given alignment of P and T, a substring t of T matches a suffix of P 
    and suppose t is the largest such substring for the given alignment.
    <br>
    >1. Then find, if it exists, the right-most copy t′ of t in P such that 
    t′ is not a suffix of P and the character to the left of t′ in P 
    differs from the character to the left of t in P. 
    Shift P to the right so that substring t′ in P aligns with substring t in T.
    <br><br>
    >2. If t′ does not exist, then shift the left end of P to the right by the least amount 
    (past the left end of t in T) so that a prefix of the shifted pattern matches a suffix of t in T. 
    This includes cases where t is an exact match of P. 
    <br><br>
    >3. If no such shift is possible, then shift P by m (length of P) places to the right.
  

- **Example 1:**
  - Let _T_ := _B A O B A B_
  - Then _GST_ :=

      | $k$ |                   |     |     |                   |     |               | $d2$           |
      |-----|-------------------|-----|-----|-------------------|-----|---------------|----------------|
      |     | 0                 | 1   | 2   | 3                 | 4   | 5             |                |
      |     | _B_               | _A_ | _O_ | _B_               | _A_ | _B_           |                |
      |     |                   |     |     |                   |     |               |                |
      | 1   |                   |     |     | _B_<sup> s*</sup> |     | <sup>s*</sup> | abs(5 - 3) = 2 |
      | 2   | _B_<sup> *p</sup> |     |     |                   |     | <sup>*p</sup> | abs(5 - 0) = 5 |
      | 3   | _B_<sup> *p</sup> |     |     |                   |     | <sup>*p</sup> | abs(5 - 0) = 5 |
      | 4   | _B_<sup> *p</sup> |     |     |                   |     | <sup>*p</sup> | abs(5 - 0) = 5 |
      | 5   | _B_<sup> *p</sup> |     |     |                   |     | <sup>*p</sup> | abs(5 - 0) = 5 |

- **Example 2:**
  - Let _T_ := _W O W W O W_
  - Then _GST_ :=

      | $k$ |                   |     |     |                   |     |               | $d2$           |
      |-----|-------------------|-----|-----|-------------------|-----|---------------|----------------|
      |     | 0                 | 1   | 2   | 3                 | 4   | 5             |                |
      |     | _W_               | _O_ | _W_ | _W_               | _O_ | _W_           |                |
      |     |                   |     |     |                   |     |               |                |
      | 1   |                   |     |     | _W_<sup> s*</sup> |     | <sup>s*</sup> | abs(5 - 3) = 2 |
      | 2   | _W_<sup> *p</sup> |     |     |                   |     | <sup>*p</sup> | abs(5 - 0) = 5 |
      | 3   | _W_<sup> s*</sup> |     |     | <sup>s*</sup>     |     |               | abs(3 - 0) = 3 |
      | 4   | _W_<sup> *p</sup> |     |     | <sup>*p</sup>     |     |               | abs(3 - 0) = 3 |
      | 5   | _W_<sup> *p</sup> |     |     | <sup>*p</sup>     |     |               | abs(3 - 0) = 3 |
    
    See video explanation for this particular example [here](https://www.youtube.com/watch?v=GoDHFZUuVpY) 


- **References/Resources** (covers heuristic constructions):
  - _Introduction to the Design and Analysis of Algorithms by Anany Levitin (Chapter 7)_
  - _Concise [presentation slides](https://www.collegesidekick.com/study-docs/4797428) 
      by Houssain Kettani, based off Anany Levitin's book_

# 6. Tries

### Standard Tries

A trie is a tree-like data structure for storing the characters in a word/string and allowing a wide range
of queries and matching operations. The root node always contain the empty string character,
Other nodes contain a single character. 

The leaf nodes in a standard trie represent the total number of words in that trie. 
The trie also aims to encourage node reuse when possible, by adding _terminals_ 
(usually deleanated by empty ndoes) along each path from the root, to indicate that a search query 
can correctly terminate at that node without traversing until it arrives at a leaf.

### Compressed Tries

Ordinary tries are easy to comprehend. Compressed tries take things a bit further but complications
only arise in the wake of linear time construction. A compressed trie reduces the number of nodes
in a standard trie, but the overhead of the number of characters remain unchanged.
This can be mitigated however, by storing indices instead of the characters themselves.

Other extension of (compressed) tries are **suffix tries**, of which the linear time construction 
can be produced by **Ukkonen Algorithm**, which adds **suffix links** to the resulting suffix trie.
This addition allows complex queries such as containment, substring length, and frequency.

### Suffix Links

Suffix link is a directed edge from a node $`i`$ to a node $`j`$ in a suffix tree such that, 
if the total characters on an edge culminating in a node $`i`$ is $`x\alpha[...]`$, 
then a suffix link can be extended from $`i`$ to some other node $`j`$ culminating with $`\alpha[...]`$.

**Suffix links are particularly useful in determining the longest substring of a 
query that exists in a text** ([see demonstration](https://www.youtube.com/watch?v=k6VJW6hzDZQ)).

### Suffix Arrays

Alternative to suffix trie is the **suffix array** which reduces complexity on the constant 
overhead and space usage. Suffix arrays allow for quasi-binary search optimality during queries, 
based on the fact that it is **_already_ lexicographically sorted**. We can recur either backwards
(when we encounter a mismatched character that is lexicographically higher) or forwards 
(when lexicographically lower).

Once we recur and arrive at a new midpoint, the length of the longest common prefix (LCP) between
the query and most recent match implies that the entry at the current position is also at least 
the size of the LCP itself, which allows us to skip this number of comparisons upon the 
next matching candidate.

The most interesting auxiliary heuristic data strcuture complementing the suffix array, is the
**LCP Array**, which computes the length of the longest common prefix between every consecutive
pair of suffixes sorted in the suffix array.


### Ukkonen Algorithm

**Rule 1:**

If the path from the root labelled $`S[i... j]`$ ends at a leaf edge (i.e. $`S[j]`$ is the last
character on leaf edge) then character $`S[j+1]`$ is just added to the end of the label.

**Rule 2:**

If the path from the root labelled $`S[i... j]`$ ends at a non-leaf edge (i.e. there are more
characters after $`S[i+1]`$ on path), and next character is not $`S[j+1]`$, then a new leaf edge
with label $`S[j+1]`$ and character $`j`$ is created starting from character $`S[j+1]`$.
A new internal node will also be created if $`S[j+1]`$ ends inside (in-between) a non-leaf edge.

**Rule 3:**

If the path from the root labelled $`S[i... j]`$ ends at non-leaf edge (i.e. there are more
characters after $`S[i]`$ on path), and next character is $`S[i+1]`$ (already in tree), do nothing.

#### References/Resources

- [Trie - Wikipedia](https://en.wikipedia.org/wiki/Trie)
- [Suffix Tree - Wikipedia](https://en.wikipedia.org/wiki/Suffix_tree)
- [Suffix Array - Wikipedia](https://en.wikipedia.org/wiki/Suffix_array)
- [LCP Array - Wikipedia](https://en.wikipedia.org/wiki/LCP_array)
- [(SAIS) Suffix Array Induced-Sorting - Nong, Zang & Chang (2009)](https://ieeexplore.ieee.org/document/4976463)
- [(SAIPS) _Optimal In-Place Suffix Sorting_ - Li, Li & Huo (2016)](https://arxiv.org/abs/1610.08305)
- [YouTube Playlist by Ben Langmead - _Suffix Indexing_](https://www.youtube.com/playlist?list=PL2mpR0RYFQsDFNyRsTNcWkFTHTkxWREeb)
- [YouTube Video - _Linear Time Suffix Array Construction via SAIS_](https://www.youtube.com/watch?v=yb0Os_MTU_4)
- [Suffix Array and LCP Generator](https://visualgo.net/en/suffixarray)
- [Ukkonen Visualizer](http://brenden.github.io/ukkonen-animation/)
- [Applications of Suffix Array and LCPs](https://mediathek.hhu.de/watch/b4d092e2-06ba-4786-abe4-7ffc614b2244#)
