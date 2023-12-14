# Binary Search Trees

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
