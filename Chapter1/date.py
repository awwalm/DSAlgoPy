"""Implements a proleptic Gregorian calendar date as a Julian day number."""


# noinspection PyProtectedMember
import logging
import math

# Configuring default logging behaviour
logging.basicConfig()
logging.root.setLevel(logging.NOTSET)


# noinspection PyProtectedMember
class Date:
    """
    Creates an object instance for the specified Gregorian date.
    B.C. dates are created with years expressed in negative integers.
    """

    def __init__(self, month, day, year):
        self._julianDay = 0
        assert self._isValidGregorian(month, day, year), f"Invalid Gregorian Day: {month, day, year}"

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
        # Cheers to GitHub user Ithebe for this fix (https://github.com/lthebe/PythonDS)
        return ((13 * month + 3) // 5 +
                day + year + year // 4 -
                year // 100 + year // 400) % 7

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

    def monthName(self) -> str:
        """Returns a string containing the name of the month."""
        month_names = {1: "January", 2: "February", 3: "March", 4: "April",
                       5: "May", 6: "June", 7: "July", 8: "August",
                       9: "September", 10: "October", 11: "November", 12: "December"}
        return month_names[self.month()]

    def isLeapYear(self) -> bool:
        """Determines if this date falls in a leap year and returns the appropriate boolean value."""
        return self.year() % 4 == 0

    def numDays(self, otherDate):
        """Returns the number of days as a positive integer between this date and the ``otherDate``."""
        if self.year() == otherDate.year() and self.month() == otherDate.month():
            return abs(self.day() - otherDate.day())
        logging.warning("numDays(): Only compatible with dates within same year at the moment.")

    # noinspection PyMethodMayBeStatic
    def _isValidGregorian(self, month, day, year) -> bool:
        """Validates the Gregorian date based on user input constructed by ``Date(month, day, year)``."""

        # Validate year
        y_valid = -4714 < year < +math.inf

        # Validate day
        thirty_days = [9, 4, 6, 11]
        if month == 2:
            d_valid = day in range(1, 29 + 1) if year % 4 == 0 else day in range(1, 28 + 1)
        elif month in thirty_days:
            d_valid = day in range(1, 30 + 1)
        else:
            d_valid = day in range(1, 31 + 1)

        # Validate month
        m_valid = month in range(1, 12 + 1)
        if year == -4713:
            m_valid = month in range(1, 11 + 1)
            if month == 11:
                d_valid = day in range(1, 24 + 1)

        return m_valid and d_valid and y_valid

    def dayOfWeekName(self) -> str:
        """Returns a string containing the name of the day."""
        day_names = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
                     4: "Friday", 5: "Saturday", 6: "Sunday"}
        return day_names[self.dayOfWeek()]

    def advanceBy(self, days: int):
        """Advances the date by the given number of days.
         The date is incremented if days is positive and decremented if days is negative."""

        assert isinstance(days, int), "Day parameter must be integer type"

        # {1:31, 2:[28,29], 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        accum_days = {1: [31, 31, 31, 31], 2: [59, 60, 28, 29], 3: [90, 91, 31, 31],
                      4: [120, 121, 30, 30], 5: [151, 152, 31, 31], 6: [181, 182, 30, 30],
                      7: [212, 213, 31, 31], 8: [243, 244, 31, 31], 9: [273, 274, 30, 30],
                      10: [304, 305, 31, 31], 11: [334, 335, 30, 30], 12: [365, 366, 31, 31]}
        the_day, the_month, the_year = self.day(), self.month(), self.year()
        the_accum_days = accum_days[the_month-1][0 if self.isLeapYear() else 1] + the_day
        logging.info(f"advanceBy(): Initial accummulated days: {the_accum_days}")

        # If we're handling A.D./C.E. years and not negative (B.C./B.C.E.) years.
        if the_year > 0 and days > 0:
            while days != 0:
                # Ensure the DAY is not incremented past the allowed limit.
                if the_day < accum_days[the_month][2 if the_year % 4 == 0 else 3]:
                    the_day += 1
                    the_accum_days += 1
                if the_day >= accum_days[the_month][2 if the_year % 4 == 0 else 3]:
                    the_day = 1
                    the_month = the_month + 1 if the_month <= 11 else 1
                # If we are on the last day of the given MONTH, progress to the next one.
                days_in_month = accum_days[the_month][2 if the_year % 4 == 0 else 3]
                if the_day == days_in_month:
                    the_month = the_month + 1 if the_month < 11 else 1
                # If we are on the last day of the YEAR, reset accum_days (for leap/normal years).
                if the_year % 4 == 0:
                    the_year = the_year + 1 if the_accum_days == 366 else the_year
                    the_accum_days = 0 if the_accum_days == 366 else the_accum_days
                if the_year % 4 != 0:
                    the_year = the_year + 1 if the_accum_days == 365 else the_year
                    the_accum_days = 0 if the_accum_days == 365 else the_accum_days
                # Decrease the count of days
                days -= 1

        logging.info(f"advanceBy(): Total accummulated days: {the_accum_days + days}")
        return Date(the_month, the_day, the_year)
