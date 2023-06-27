# Notes

## Chpater 2: Object-Oriented Programming

- **Design Pattern**:
<br>
A pattern provides a general template for a solution that can be applied in many situations. 
It describes the **main elements** of a solution in an abstract way that can be specialized 
for a specific problem at hand. It consists of a **name**, which identifies the pattern; 
a **context**, which describes the scenarios for which this pattern can be applied; 
a **template**, which describes how the pattern is applied; 
and a **result**, which describes and analyzes what the pattern produces.
<hr>

- **Dictionaries and the `__slots__` Declaration**:
<br>
By default, Python represents each namespace with an instance of the built-in `dict` class
that maps identifying names in that scope to the associated objects. A dictionary requires
additional memory beyond raw data contained in it. We avoid this inefficiency caveat by 
representing instance namespaces as string sequences (technically a `tuple`) assigned to
a class-level member called `__slots__`.
<br>
Sublcasses whose parents declare `__slots__` must declare it too, however, only additional
instance members must be provided. 

## Chpater 7: Linked Lists

- **Implemening Stacks and Queues via Linked Lists**:
<br>
Each `_Node` object [^1],[^2] used in structuring the linked list is unaware if it's the head or tail node. 
Only the controller or linked list object knows the head and tail references.
<hr>

- **The Positional List ADT**:
<br>
As useless as it seems (this assumption proves to be ultimately true as the ADT serves no unique purpose), 
this data structure is just a facility for inserting and removing at any location in a doubly linked list.
It can be argued that the accessing a specific node (which at this time of writing) via a selected routine
can be done in constant time, but I maitain the position that this is **NOT** <i>O</i>(1) time however.
<br>
<blockquote>Consider continuously reassigning a node variable to the next node until the correct one is detected.
Is this any different from iterating until arriving at an item (<i>O(m <= n)</i>) ? Or perhaps, do we approximate 
this to "constant time instant retrieval" (<i>O(k >= 1)</i>) ?</blockquote>

# References

[^1]: [`linked_queue.py#LinkedQueue#_Node`](/Goodrich/Chapter7/linked_queue.py) <br>
[^2]: [`linked_stack.py#LinkedStack#_Node`](/Goodrich/Chapter7/linked_stack.py)