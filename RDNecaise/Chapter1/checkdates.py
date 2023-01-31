"""
# Extracts a collection of birth dates from the user and determines
# if each individual is at least 21 years of age.
"""
import datetime
from date import Date


def main():
    # Date before which a person must have been born to be 21 or older.
    bornBefore = Date(6, 1, datetime.date.today().year-21)

    # Extract birth dates from the user and determine if 21 or older
    date = promptAndExtractDate()
    while date is not None:
        if date <= bornBefore:
            print("Is at least 21 years of age: ", date)
        date = promptAndExtractDate()


def promptAndExtractDate():
    """Prompts for and extracts the Gregorian date components. Returns a
    Date object or None when the user has finished entering dates."""

    print("Enter a birth date.")
    month = int(input("month (0 to quit): "))
    if month == 0:
        return None
    else:
        day = int(input("day: "))
        year = int(input("year: "))
        return Date(month, day, year)


# Call the main routine.
if __name__ == '__main__':
    main()
