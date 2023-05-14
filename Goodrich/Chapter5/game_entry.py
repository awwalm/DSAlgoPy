"""Code Fragment 5.7: Python code for a simple ``GameEntry`` class.
We include methods for returning the name and score for a game entry object, 
as well as a method for returning a string representation of this entry.\n

Code Fragment 5.8: Python code for a ``Scoreboard`` class that maintains
an ordered series of scores as GameEntry objects.
"""

from typing import List


class GameEntry:
	"""Represents one entry of a list of high scores."""

	def __init__(self, name, score):
		self._name = name
		self._score = score

	def get_name(self):
		return self._name

	def get_score(self):
		return self._score

	def __str__(self):
		return "({0}, {1:2d})".format(self._name, self._score)


class Scoreboard:
	"""Fixed-length sequence of high scores in nondecreasing order."""
	def __init__(self, capacity=10):
		""" All enteries are initially None."""
		# self._board = [None] * capacity
		self._board: List[GameEntry] = [GameEntry(None, None)] * capacity  # Takes care of linter warning
		self._n = 0

	def __getitem__(self, k):
		"""Return entry at index ``k``."""
		return self._board[k]

	def __str__(self):
		"""Return string representation of the high score list."""
		return "\n".join(str(self._board[j]) for j in range(self._n))

	def add(self, entry):
		"""Consider adding entry to high scores."""
		score = entry.get_score()

		#: Does new entry qualify as a high score?
		#: Answer is YES if board not full or score is higher than last entry.
		good = self._n < len(self._board) or score > self._board[-1].get_score()

		if good:
			if self._n < len(self._board):		# No score drops from list.
				self._n += 1					# So overall number increases.
