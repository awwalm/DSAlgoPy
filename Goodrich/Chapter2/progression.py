"""Demonstration of hierarchical programming using a base class called ``Progression.``"""
from overrides import override


class Progression:
	"""Iterator producing a generic progression.
	Default iterator produces the whole numbers 0,1,2,..."""

	def __init__(self, start=0):
		"""Initialize current to the first value of the progression."""
		self._current = start

	def _advance(self):
		"""Udate self._current to a new value.
		This should be overriden by a subclass to customize progression.
		By convention, if current is set to ``None`` (end of finite progression).
		"""
		self._current += 1

	def __next__(self):
		"""Return the next element, or else raise ``StopIteration`` error."""
		if self._current is None:			# Our convention to end a progression.
			raise StopIteration()
		else:
			answer = self._current			# Record current value to return.
			self._advance()					# Advance to prepare for next time.
			return answer

	def __iter__(self):
		"""By convention, an iterator must return itself as an iterator."""
		return self

	def print_progression(self, n):
		"""Print next n values of the progression."""
		print(" ".join(str(next(self)) for _ in range(n)))


class ArithmeticProgression(Progression):
	"""Iterator producing an arithmetic progression."""

	def __init__(self, increment=1, start=0):
		"""Create a new arithmetic progression.\n
		:param increment:	The fixed constant to add to each term (default 1).
		:param start:		The first term of the progression (default 0).
		"""
		super().__init__(start)				# Initialize base class.
		self._increment = increment

	def _advance(self):						# Override inherited version.
		"""Update current value by adding the fixed increment."""
		self._current += self._increment


class GeometricProgression(Progression):  	# Inherit from Progression.
	"""Iterator producing a geometric progression."""

	def __init__(self, base=2, start=1):
		"""Create a new geometric progression.\n
		:param base:	The fixed constant multiplied to each term (default 2).
		:param start:	The first term of the progression (default 1).
		"""
		super().__init__(start)
		self._base = base

	@override
	def _advance(self):						# Override inherited version.
		"""Update current value by multiplying it by the base value."""
		self._current *= self._base


class FibonacciProgression(Progression):
	"""Iterator producing a generalized Fibonacci progression."""

	def __init__(self, first=0, second=1):
		"""Create a new Fibonacci progression.\n
		:param first:	The first term of the progression (default 0).
		:param second:	The second term of the progression (default 1).
		"""
		super().__init__(first)				# Start progression at first.
		self._prev = second - first			# Fictitious value preceding the first.

	def _advance(self):
		"""Update current value by taking sum of previous two."""
		self._prev, self._current = self._current, self._prev + self._current
