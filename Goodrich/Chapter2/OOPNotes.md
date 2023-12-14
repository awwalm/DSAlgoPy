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