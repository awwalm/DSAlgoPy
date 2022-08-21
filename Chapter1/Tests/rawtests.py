import datetime
from Chapter1.date import Date


def main():
    # Date before which a person must have been born to be 21 or older.
    the_date = Date(datetime.date.today().month,
                    datetime.date.today().day,
                    datetime.date.today().year)
    print(the_date)
    print(the_date.dayOfWeekName())
    print(the_date.monthName())

    other_date = Date(8, 25, 2022)
    print(the_date.numDays(other_date))

    bc_date = Date(11, 24, -4713)
    print(bc_date.numDays(other_date))


if __name__ == "__main__":
    main()
