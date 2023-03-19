"""
Our first algorithm for computing prefix averages, named prefix average1,
is shown in Code Fragment 3.2. It computes every element of A separately, 
using an inner loop to compute the partial sum.
"""


def prefix_average1(S):
	"""Return list such that, for all `j`, `A[j]` equals average of S[0],..., S[j].\n
	:param S: A sequence of randomly arranged integers.
	"""
	n = len(S)
	A = [0] * n 					# Create new list of n zeroes.
	for j in range(n):
		total = 0					# Begin computing S[0] + ... + S[j].
		for i in range(j + 1):
			total += S[i]
		A[j] = total / (j+1)		# Record the average.
	return A
