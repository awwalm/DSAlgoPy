"""Functional style Prefix Trie implementation."""
from Goodrich.Chapter13.Tries.compressed_trie import CompressedTrie


def prefix_tree(X):
    """Builds a Compressed Trie on the set of prefixes of X."""
    pref = []
    j = len(X)
    while j > 0:
        pref.append(X[0:j])
        j -= 1
    pt = CompressedTrie()
    pt.build(pref)
    return pt


def test_prefix_trie(S):
    t = prefix_tree(S)
    prefixes = [S[0:i] for i in range(1, len(S)+1)]
    BS = [S[::-1], S[len(S)//2:]+S[:len(S)//2]]
    print(f"\nPrefix Trie size (nodes): {len(t)}")
    print(f"Prefix Trie count (total characters): {t.count()}")

    # Array representation of Prefix Trie
    print(f"Prefix Trie levels:")
    for i in [L for L in t.bfs()]:
        print(i)
    print()

    # Successful searches for strings in Prefix Trie
    for s in prefixes:
        print(f"`{s}` in Prefix Trie: {t.find(s)}")
    print()

    # Unsuccessful or partial searches for strings in (or not in) Prefix Trie
    for bs in BS:
        print(f"`{bs}` in Prefix Trie: {t.find(bs)} ")

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
    for p in patterns: test_prefix_trie(p)

