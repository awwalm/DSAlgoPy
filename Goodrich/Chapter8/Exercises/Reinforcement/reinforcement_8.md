## R-8.6
> Let _T_ be an _n_-node binary tree that may be **improper**. Describe how to represent _T_ by means of a **proper** binary tree _T'_ with _O_(_n_) nodes.

### Preliminaries:
- An Improper Binary Tree is a binary tree with each node having a range of 0 to 1 and 2 children.
- A Proper Binary Tree is a binary tree where each node has exactly 2 or zero children.

### Proposed Solution:

A tempting solution is to naively prepend a "null" node to every interior node having less than 2 child nodes,
 while this will still result in _O_(_n_) time, it is inherently less efficient in practicality 
(what if a million of those nullified insertions are required?), this brings us to the preferred routine as follows.

This routine executes at an exact/precise worst case of O(n+1) nodes depending on the initial number of nodes. 
Consider the following:
- If binary tree _T_ , which may be improper, contains _n_ nodes, then _T'_ is a proper binary 
tree with _O_(_n_) nodes representing _T_ if and only if: 
    - _O_(_n_) = _n_ + 1 when _n_ is even.
    -  _O_(_n_) = _Θ_(_n_) = n when _n_ is odd.

### Justification:

- In the case that tree _T_ is **improper**, this incites the possibility of _n_ being even.
- If _n_ is even, it is inherently impossible to represent _T_ as a **proper** binary tree _T'_ with _O_(_n_) nodes.
- This is because an interior node at the penultimate level of the resulting proper binary tree attempt 
will have only one child, thus invalidating the "proper" characteristic.
- The compromise is just a single additional child that carries the same value but with an alternate sign (+ or -), 
hence differentiating it from the original.
- This slight modification incites the  _Θ_(_n_) = _n_ + 1 cost.

### Compromise:

The corresponding proper binary tree will produce an equivalent sequence when traversed using a PREORDER algorithm. 
The structure and level however, would change. If in the application or use-case, structural consistency is required, 
then the less-favorable routine of "nullification" ought to be considered but with great cost incurred.

### Algorithm "_REPRESENT AS PROPER BINARY TREE(Binary Tree)_":

1. For each node in the original improper tree, create a new node in the proper binary tree.
2. For each child node of a node in the original tree, consider it as the left child of its parent.
3. For each subsequent child of the same parent in the original tree, consider it as the right sibling 
of the previous child in the proper binary tree.
4. If no second child, consider the immediate descendant as the right child in the proper binary tree.
5. If the number of nodes in the original improper binary tree is even, add a node with the same absolute value 
but with the opposite sign to the last single node to balance the tree.
6. [_OPTIONAL_] Verify the sequence from both trees by a PREORDER traversal to ensure consistency of output. 
7. Simply disregard the last element in the PREORDER sequence of _T'_ if _T_ contained even _n_ nodes.

### Visualization:

- Original Improper Binary Tree: Let _T_ be the following, with _n_ = 6
```
    1
   / \
  2   3
 /     \
5       4
 \
  6
```

- Corresponding Proper Binary Tree: We obtain _T'_, with nodes such that  _O_(_n_) = _n_ + 1 = 7
```
    1
   /  \
  2    3
 / \   / \
5  6  4  -4

```
- PREORDER(_T_) := [1, 2, 5, 6, 3, 4]
- PREORDER(_T'_) := [1, 2, 5, 6, 3, 4, _-4_]


## R-8.7
> What are the minimum and maximum number of internal and external nodes 
in an improper binary tree with n nodes?

### The Trick:
Note that the maximum possible capacity of an improper binary tree is a perfect binary tree with one node short.

### Proposed Solution:

Given an arbitrary binary tree _T_:
- Let _h_ denote the height
- Let _n_ be the number of nodes
- Let _n<sub>I</sub>_ be the number of internal nodes
- Let _n<sub>L</sub>_ be the number of leaf nodes
- Let _max<sub>P</sub>_ or _min<sub>P</sub>_ be "maximum or minimum possible".

1. **If _T_ is a proper binary tree**:
   1. _max<sub>P</sub>_(_n_) = 2<sup>(h+1)</sup> - 1 (**perfect** binary tree)
   2. _min_(_n_) = 1 (singleton node/root)
   3. _max<sub>P</sub>_(_n<sub>I</sub>_) = _n_ - _n<sub>L</sub>_ = 2<sup>h</sup> - 1
   4. _min_(_n<sub>I</sub>_) = 0 (singleton/root with no interior nodes and no children)
   5. _max_(_n<sub>L</sub>_) = 2<sup>h</sup> (i.e. a **perfect** binary tree is the limit)
   6. _min_(_n<sub>L</sub>_) = 0 (same conditions as [iv])

2. **If _T_ is an improper binary tree**:
   1. _max<sub>P</sub>_(_n_) = 2<sup>(h+1)</sup> - 2 (i.e. one node short of being a perfect binary tree is the most it takes to be improper)
   2. _min_(_n_) = 1
   3. _max<sub>P</sub>_(_n<sub>I</sub>_) = 2<sup>h</sup> - 1 (an improper tree can be proper until the penultimate tree level)
   4. _min<sub>P</sub>_(_n<sub>I</sub>_) = {1 when _n_ = 2 | _h_ when _n_ >= 2}
   5. _max_(_n<sub>L</sub>_) = 2<sup>h</sup> - 1 (one node short of the leaves in a perfect binary tree)
   6. _min_(_n<sub>L</sub>_) = 1 (just the root, i.e. singleton)

3. We subsequently derive the following using **double counting** techniques:
   - Let _n<sub>0</sub>_ be the number of nodes with no children (i.e. _n<sub>0</sub>_= _n<sub>L</sub>_)
   - Let _n<sub>1</sub>_ be the number of nodes with 1 child (i.e. _n<sub>1</sub>_ >= 1)
   - Let _n<sub>2</sub>_ be the number of nodes with 2 children
   1. _n_ = _n<sub>0</sub>_ + _n<sub>1</sub>_ + _n<sub>2</sub>_
   2. Nodes in the tree that are children of another node is _n_ - 1
   3. The number of child nodes that have a parent with 2 children is _2n<sub>2</sub>_
   4. This follows that _n_ - 1 = _n<sub>1</sub>_ + _2n<sub>2</sub>_
   5. From [i], _n<sub>2</sub>_ = _n_ - _n<sub>0</sub>_ - _n<sub>1</sub>_
   6. Substituting in [iv], _n_ - 1 = 2(_n_ - _n<sub>0</sub>_ - _n<sub>1</sub>_)
   7. So that _2n<sub>0</sub>_ = _n_ - _n<sub>1</sub>_ + 1
   8. When _n_ is even, _min<sub>P</sub>_(_n_<sub>1</sub>) = 1
   9. When _n_ is odd, _min<sub>P</sub>_(_n_<sub>1</sub>) = 2
   10. **The maximum number of external nodes:** _max_(_n<sub>L</sub>_) = _floor_(_n_ / 2)
   11. **The minimum number of external nodes:** _min_(_n<sub>L</sub>_) = 1
   12. **The maximum number of internal nodes when _n_ is even:** _max_(_n<sub>I</sub>_) = _max_(_n<sub>L</sub>_) + 1 = _floor_(_n_ / 2) + 1
   13. **The maximum number of internal nodes when _n_ is odd:** _max_(_n<sub>I</sub>_) = _max_(_n<sub>L</sub>_) + 2 = _floor_(_n_ / 2) + 2
   14. **The minimum number of internal nodes:** _min_(_n<sub>I</sub>_) = _h_


## R-8.20
> Draw a binary tree _T_ that simultaneously satisfies the following:
>   - Each internal node of _T_ stores a single character.
>   - A _preorder_ traversal of _T_ yields EXAMFUN.
>   - An _inorder_ traversal of _T_ yields MAFXUEN.
```
          E
         / \
        X   N
       / \    
      A   U    
     / \
    M   F
```
