import datetime
from Chapter1.date import Date


def main():
    # Date before which a person must have been born to be 21 or older.
    the_date = Date(datetime.date.today().month,
                    datetime.date.today().day,
                    datetime.date.today().year)
    print(f"TODAY'S DATE: {the_date}")
    print(f"DAY OF WEEK: {the_date.dayOfWeekName()}")
    print(f"NAME OF MONTH: {the_date.monthName()}")

    other_date = Date(8, 25, 2022)
    bc_date = Date(11, 24, 4713)
    print(f"OTHER DATE: {other_date}")
    print(f"DIFFERENCE BETWEEN TODAY and other_date: {the_date.numDays(other_date)}")

    print(f"NUMBER OF DAYS ELAPSED IN YEAR: {the_date.dayOfYear()}")
    print(f"ADVANCE TODAY'S DATE BY 365 DAYS: {the_date.advanceBy(365)}")

    print(f"AS GREGORIAN: {the_date.asGregorian('-')}")


if __name__ == "__main__":
    main()
