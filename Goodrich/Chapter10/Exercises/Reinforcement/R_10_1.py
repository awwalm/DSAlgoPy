"""R-10.1 Give a concrete implementation of the pop method in the context of the MutableMapping class,
relying only on the five primary abstract methods of that class."""
import random
from collections.abc import MutableMapping


# noinspection PyPep8Naming
class _(MutableMapping):

    def pop(self, __key=None):
        if len(self) == 0:
            raise KeyError("Can't pop from empty map")
        elif __key is None:
            k = random.randint(0, len(self)-1)
            deleted = self[list(self.keys())[k]]      # Russian Roullette
            del self[list(self.keys())[k]]
            return deleted
        elif __key in self.keys():
            deleted = self[__key]
            del self[__key]
            return deleted
        else:
            raise KeyError("No such key exists in map")
