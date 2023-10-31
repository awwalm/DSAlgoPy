import queue

class Queue(queue.Queue):
    """Compact subclass of the inbuilt Python ``Queue`` class."""
    super().__init__(maxsize=0)
    def enqueue(self, item):
        return self.put_nowait(item)
    def dequeue(self):
        return self.get_nowait()


class ExpressionTree:
    """Builds an expression tree for the expression string."""
    def __init__(self, expStr):
        self._expTree = None
        self._buildTree(expStr)

    def evaluate(self, varMap):
        """Evaluate the expression tree and returns the resulting value."""
        return self._evalTree(self._expTree, varMap)

    def __str__(self):
        """Returns a string representation of the expression tree."""
        return self._buildString(self._expTree)

    def _buildString(self, treeNode):
        """Recursively builds a string representation of the expression tree."""
        if treeNode.left is None and treeNode.right is None:    # If node is leaf, it's an operand.
            return str(treeNode.element)
        else:                                                   # Otherwise, it's an operator.
            expStr = str("("
                         + self._buildString(treeNode.left)
                         + str(treeNode.element)
                         + self._buildString(treeNode.right)
                         + ")")
            return expStr

    def _evalTree(self, subtree, varDict):
        """See if the node is a leaf node, in which case return its value.\n
        :param varDict: Example - ``{ 'a' : 5, 'b' : 12 }``
        """
        if subtree.left is None and subtree.right is None:      # If node is a leaf, return its value.
            if "0" <= subtree.element <= "9":                   # Is the operand a literal digit?
                return int(subtree.element)
            else:                                               # Or is it a variable?
                assert subtree.element in varDict, "Invalid variable"
                return varDict[subtree.element]
        else:                                                   # Otherwise, it's an operator to be computed.
            lvalue = self._evalTree(subtree.left, varDict)
            rvalue = self._evalTree(subtree.right, varDict)
            return self._computeOp(lvalue, subtree.element, rvalue)

    def _buildTree(self, expStr):
        """Build a queue containing the tokens in the expression string."""
        expQ = Queue()
        for token in expStr:
            expQ.enqueue(token)
        self._expTree = _ExpTreeNode(None)                      # Create an empty root node.
        self._recBuildTree(self._expTree, expQ)                 # Recursively build expresson tree.

    def _recBuildTree(self, curNode, expQ):
        """Recursively builds the tree given an initial root node."""
        token = expQ.dequeue()                                  # Extract the next token from the queue.
        if token == "(":                                        # If token is a left parent.
            curNode.left = _ExpTreeNode(None)
            self._recBuildTree(curNode.left, expQ)
            curNode.data = expQ.dequeue()                       # Next token will be an operator: +-/*%
            curNode.right = _ExpTreeNode(None)
            self._recBuildTree(curNode.right, expQ)
            expQ.dequeue()                                      # Next token will be a ")", remove it.
        else:                                                   # Else, token is a digit, convert it to int.
            curNode.element = token

    def _computeOp(self, left, op, right):
        """Compute the arithmetic operation based on the supplied op string."""


class _ExpTreeNode:
    """Storage class for creating the tree nodes."""
    def __init__(self, data):
        self.element = data
        self.left = None
        self.right = None
