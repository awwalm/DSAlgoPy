"""Tests for the KMP algorithm and failure function."""

from Goodrich.Chapter13.PatternMatching.KnuthMorrisPratt.kmp import *

p = "AAACAAAA"
ftable = compute_kmp_fail(p)
print(ftable)

