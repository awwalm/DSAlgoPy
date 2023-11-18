# Notes

## Supporting Material (Similar Repos & Solved Problems)

- [Charles Reid's DSA/ML Repo with Java Solutions](https://github.com/charlesreid1/java)
- [Jihoon Kim's Worked Solutions (Till Chapter 8)](https://github.com/jihoonerd/Data_Structures_and_Algorithms_in_Python)
- [William Cameron's Solutions (Till Chapter 6)](https://github.com/wdlcameron/Solutions-to-Data-Structures-and-Algorithms-in-Python)

## Chpater 2: Object-Oriented Programming

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


## Chpater 7: Linked Lists

- **Implemening Stacks and Queues via Linked Lists**:
Each `_Node` object [^1],[^2] used in structuring the linked list is unaware if it's the head or tail node. 
Only the controller or linked list object knows the head and tail references.


- **The Positional List ADT**:
As useless as it seems (this assumption proves to be ultimately true as the ADT serves no unique purpose), 
this data structure is just a facility for inserting and removing at any location in a doubly linked list.
It can be argued that the accessing a specific node (which at this time of writing) via a selected routine
can be done in constant time, but I maintain the position that this is **NOT** _O_(1) time however.
  >Consider continuously reassigning a node variable to the next node until the correct one is detected.
  Is this any different from iterating until arriving at an item (_O(m <= n)_) ? Or perhaps, do we approximate 
  this to "constant time instant retrieval" (_O(k >= 1)_) ?


- **Implementing _Proper_ Linked Lists**:
  - Most of the conceptual "linked list" programs (or classes) in the book are private **base** classes.
  The use of a proper or standard (whichever term you prefer) linked list implies two things:
  re-inventing the wheel (re-writing your own classes); extending an abstraction over the base classes.
  - I've gone for a better and rigid approach - implementing the classes by reusing the patterns and structures
  from the base classes provided in the book, starting with the singly linked list, and then extending 
  all other variants (doubly, circular, etc.) cascadingly or non-sequentially as desired.
  - This comes with several challenges such as dealing with dichotomies of Python's more obscure inheritance syntax.
  Nothing that can't be handled by enforcing D.R.Y. principles (so far) and coverage tests.


## Chapter 10: Maps, Hash Tables, and Skip Lists
- **See [HashingNotes.md](Chapter10/HashingNotes.md)**
  
[^1]: See class/method: [`linked_queue.LinkedQueue._Node`](../Goodrich/Chapter7/linked_queue.py)

[^2]: See class/method: [`linked_stack.LinkedStack._Node`](../Goodrich/Chapter7/linked_stack.py)