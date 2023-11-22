
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
for the characters of a string delimited by the tuple $`( x_0 , x_1, x_2, \ldots, x_{n-1} )`$ as

```math
\begin{align*}
   h(x) := 
\end{align*}
```
