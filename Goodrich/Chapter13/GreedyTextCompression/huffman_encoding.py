"""The Huffman (En)Coding Algorithm."""
from collections import OrderedDict
from Goodrich.Chapter13.GreedyTextCompression.min_heap import MinHeap
from Goodrich.Chapter13.GreedyTextCompression.utils import print_tree


def huffman(X: str):
    f = OrderedDict()
    Q = MinHeap()

    for c in X:
        if not f.get(c):
            f[c] = X.count(c)
            t = Q.Node(key = c, value = c, parent = None)
            Q.insert(k=f[c], v=t)

    while len(Q) > 1:
        f1, T1 = Q.remove_min()
        f2, T2 = Q.remove_min()
        T = Q.Node(key = f1+f2, value = f1+f2, parent = None)
        T.left = T1
        T.right = T2
        Q.insert(k=f1+f2, v=T)

    F, T = Q.remove_min()
    return T, f


def test_huffman(x: str):
    huff_tree, frequency = huffman(X=x)

    print("\nFrequency Table")
    maxpad = len(str(max(frequency.values())))
    chars =  "| %-9s ||" % "Character"
    counts = "| %-9s ||" % "Frequency"
    for k, v in zip(frequency.keys(), frequency.values()):
        top = " %-*c |" % (maxpad, k)
        bottom = " %-*s |" % (maxpad, frequency[k])
        chars += top
        counts += bottom

    print("_" * len(chars))
    print(chars)
    print("-" * len(chars))
    print(counts)
    print("=" * len(counts))

    print_tree(huff_tree)


if __name__ == "__main__":
    test_huffman(x = "a fast runner need never be afraid of the dark")
