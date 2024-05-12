"""Functional style Suffix Trie implementation."""
from Goodrich.Chapter13.Tries.compressed_trie import CompressedTrie


def suffix_tree(X):
    """Builds a Compressed Trie on the set of suffixes of X."""
    suff = []
    i,j = len(X)-1, len(X)
    while i > -1:
        suff.append(X[i:j])
        i -= 1
    st = CompressedTrie()
    st.build(suff)
    return st


def test_suffix_trie(S):
    t = suffix_tree(S)
    suffixes = [S[i:len(S)] for i in range(len(S))]
    BS = [S[::-1], S[len(S)//2:]+S[:len(S)//2]]
    print(f"\nSuffix Trie size (nodes): {len(t)}")
    print(f"Suffix Trie count (total characters): {t.count()}")

    # Array representation of Suffix Trie
    print(f"Suffix Trie levels:")
    for i in [L for L in t.bfs()]:
        print(i)
    print()

    # Successful searches for strings in Suffix Trie
    for s in suffixes:
        print(f"`{s}` in Suffix Trie: {t.find(s)}")
    print()

    # Unsuccessful or partial searches for strings in (or not in) Suffix Trie
    for bs in BS:
        print(f"`{bs}` in Suffix Trie: {t.find(bs)} ")

    print("-" * 70)


if __name__ == "__main__":
    patterns = ("BANANA",
                "WOWWOW",
                "BAOBAB",
                "ABCBAB",
                "ANPANMAN",
                "10000",
                "01010",
                "DRIDI",
                "TCCTATTCTT",
                )
    for p in patterns: test_suffix_trie(p)
