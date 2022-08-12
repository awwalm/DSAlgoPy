"""Implements a proleptic Gregorian calendar date as a Julian day number."""


# noinspection PyProtectedMember
class Date:
    """Creates an object instance for the specified Gregorian date."""

    def __init__(self, month, day, year):
        self._julianDay = 0
        assert self._isValidGregorian(month, day, year), "Invalid Gregorian Day"

        # The first line of the equation, T = (M-14)/12, has to be changed
        # since Python's implementation of integer division is not the same
        # as the mathematical definition.
        tmp = -1 if month < 3 else 0
        self._julianDay = day - 32075 + \
                          (1461 * (year + 4800 + tmp) // 4) + \
                          (367 * (month - 2 - tmp * 12) // 12) - \
                          (3 * ((year + 4900 + tmp) // 100) // 4)

    def month(self):
        """Extracts the appropriate Gregorian date component."""
        return (self._toGregorian())[0]  # returning M from (M, d, y)

    def day(self):
        return (self._toGregorian())[1]  # returning D from (m, D, y)

    def year(self):
        return (self._toGregorian())[2]  # returning Y from (m, d, Y)

    def dayOfWeek(self):
        """Returns day of the week as an int between 0 (Mon) and 6 (Sun)."""
        month, day, year = self._toGregorian()
        if month < 3:
            month += 12
            year -= 1
        return ((13 * month + 3) // 5 + day + year + year // 4 - year // 400) % 7

    def __str__(self):
        """Returns the date as string in Gregorian format."""
        month, day, year = self._toGregorian()
        return "%02d/%02d/%04d" % (month, day, year)

    def __eq__(self, otherDate):
        """Logically compares the two dates (operator overloading)."""
        return self._julianDay == otherDate._julianDay

    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay

    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay

    def _toGregorian(self):
        """Returns the Gregorian date as a tuple: (month, day, year)."""
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year

    @staticmethod
    def _isValidGregorian(month, day, year) -> bool:
        """Validates the Gregorian date based on user input constructed by ``Date(month, day, year)``."""
        m_valid = month in range(1, 12 + 1)
        y_valid = -1 < year < 10000  # or len(str(year)) == 4 and year >= 0
        thirty_days = [9, 4, 6, 11]
        if month == 2:
            d_valid = day in range(1, 29 + 1) if year % 4 == 0 else day in range(1, 28 + 1)
        elif month in thirty_days:
            d_valid = day in range(1, 30 + 1)
        else:
            d_valid = day in range(1, 31 + 1)
        return m_valid and d_valid and y_valid
