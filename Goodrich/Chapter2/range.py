"""A class that mimics the built-in ``range`` class."""


class Range(object):

	def __init__(self, start, stop=None, step=1):
		"""Initialize a ``Range`` instance. Semantics is similar to built-in range class."""
		if step == 0:
			raise ValueError("Step cannot be 0")

		# Special case of range(n) should be treated as if range(0, n)
		if stop is None:								
			start, stop = 0, start	

		# Calculate the effective length once.					
		self._length = max(0, (stop - start + step - 1) // step)

		# Obtain knowledge of ``start`` & ``step`` to support ``__getitem__``.
		self._start = start
		self._step = step

	def __len__(self):
		"""Return number of entries in the range."""
		return self._length

	def __getitem__(self, k):
		"""Return entry at index ``k`` (using standard interpretation if negative)."""
		# Convert to negative index if required.
		if k < 0:
			k += len(self)

		if not 0 <= k < self._length:
			raise IndexError("Index out of range.")

		return self._start + k * self._step
