"""Solving a combinatorial puzzle by enumerating and testing all possible configurations (p. 176).

During the execution of the algorithm below, all the permutations of the three characters are generated and tested.
Note that the initial call makes three recursive calls, each of which in turn makes two more.
If we had executed ``PuzzleSolve(3,S,U)`` on a set ``U`` consisting of four elements,
the initial call would have made four recursive calls.

1. ``Algorithm PuzzleSolve(k,S,U):``
2.    Input: An integer k, sequence S, and set U
3.    Output: An enumeration of all k-length extensions to S using elements in U without repetitions
4.    for each e in U do
5.        Add e to the end of S
6.        Remove e from U                             {e is now being used}
7.        if k == 1 then
8.            Test whether S is a configuration that solves the puzzle
9.            if S solves the puzzle then
10.                return “Solution found: ” S
11.       else
12.            PuzzleSolve(k−1,S,U)                   {a recursive call}
13.       Remove e from the end of S
14.       Add e back to U                             {e is now considered as unused}
"""


def puzzle_solve(k: int, S: str, U: set):
    """Enumerates all k-length sequences S, without repitions of a given element in universe U.\n
    :param k:   The length of the expected sequences to be appended to ``S``.
    :param S:   An initially empty string of unique combination of sequences.
    :param U:   A universe of unique elements (strings) used for building sequences ``S``.
    """
    assert 0 < k <= len(U), "Sequence length not in range"
    for e in U:
        S = f"{S}{e}"
        U.remove(e)
        if k == 1:
            print(S)
        else:
            puzzle_solve(k-1, S, U)
        S = S[:-1]
        U.add(e)


puzzle_solve(3, str(), {"a", "b", "c"})
