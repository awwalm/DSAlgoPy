"""The complexity of the Fast SOE algorithm is Θ(n + sqrt(n) * log(n)).
The following code tests the growth size of sqrt(n) * log(n) against n.

Conclusion: The loose approximation shows that O(n) is the order of magnitude."""

import math


def soe_magnitude(n: int):
    print("%+6s | %+6s\n %+6s" % ("n", "sqrt(n) * log(n)", "_"*24))
    for i in range(1, n+1):
        print("%+6s | %.6f" % (i, math.sqrt(i) * math.log2(i)))

soe_magnitude(400)
