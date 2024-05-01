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


if __name__ == "__main__":
    huff_tree, frequency = huffman(X = "a fast runner need never be afraid of the dark")
    print("Frequency Table")
    for k in frequency: print(f"{k}\t:\t{frequency[k]}")
    print_tree(huff_tree)

