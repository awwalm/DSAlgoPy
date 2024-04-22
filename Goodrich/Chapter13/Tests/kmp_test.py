"""Tests for the KMP algorithm and failure function."""

from Goodrich.Chapter13.kmp import *

p = "AAACAAAA"
ftable = compute_kmp_fail(p)
print(ftable)

