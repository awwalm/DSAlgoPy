"""R-8.11 Find the value of the arithmetic expression associated with
each subtree of the binary tree of Figure 8.8."""
from Goodrich.Chapter8.expression_tree import ExpressionTree

exp1 = ExpressionTree("+", ExpressionTree("3"), ExpressionTree("1"))
exp2 = ExpressionTree("*", exp1, ExpressionTree("3"))
exp3 = ExpressionTree("-", ExpressionTree("9"), ExpressionTree("5"))
exp4 = ExpressionTree("+", exp3, ExpressionTree("2"))
exp5 = ExpressionTree("/", exp2, exp4)
exp6 = ExpressionTree("-", ExpressionTree("7"), ExpressionTree("4"))
exp7 = ExpressionTree("*", ExpressionTree("3"), exp6)
exp8 = ExpressionTree("+", exp7, ExpressionTree("6"))
output = ExpressionTree("-", exp5, exp8)
print(output.__str__())     # ((((3 +1) ×3)/((9 −5)+ 2)) − ((3 × (7−4)) +6))
print(output.evaluate())    # -13.0 (valid)
print(output.num_children(output.root()))     # 2