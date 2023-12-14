## Chpater 7: Linked Lists

- **Implemening Stacks and Queues via Linked Lists**:
Each `_Node` object [^1],[^2] used in structuring the linked list is unaware if it's the head or tail node. 
Only the controller or linked list object knows the head and tail references.


- **The Positional List ADT**:
As useless as it seems (this assumption proves to be ultimately true as the ADT serves no unique purpose), 
this data structure is just a facility for inserting and removing at any location in a doubly linked list.
It can be argued that the accessing a specific node (which at this time of writing) via a selected routine
can be done in constant time, but I maintain the position that this is **NOT** $`O(1)`$ time, however.
  >Consider continuously reassigning a node variable to the next node until the correct one is detected.
  Is this any different from iterating until arriving at an item $`O(m \leq n)`$ ? Or perhaps, do we approximate 
  this to "constant time instant retrieval" $`O(k \geq 1)`$ ?


- **Implementing _Proper_ Linked Lists**:
  - Most of the conceptual "linked list" programs (or classes) in the book are private **base** classes.
  The use of a proper or standard (whichever term you prefer) linked list implies two things:
  re-inventing the wheel (re-writing your own classes); extending an abstraction over the base classes.
  - I've gone for a better and rigid approach - implementing the classes by reusing the patterns and structures
  from the base classes provided in the book, starting with the singly linked list, and then extending 
  all other variants (doubly, circular, etc.) cascadingly or non-sequentially as desired.
  - This comes with several challenges such as dealing with dichotomies of Python's more obscure inheritance syntax.
  Nothing that can't be handled by enforcing D.R.Y. principles (so far) and coverage tests.

[^1]: See class/method: [`linked_queue.LinkedQueue._Node`](../Chapter7/linked_queue.py)

[^2]: See class/method: [`linked_stack.LinkedStack._Node`](../Chapter7/linked_stack.py)
