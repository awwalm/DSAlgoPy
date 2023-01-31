"""pgm: checkdates2.py (modified main() from checkdates.py)"""

import datetime
from checkdates import promptAndExtractDate
from linearbag import Bag
from date import Date


def main():
    bornBefore = Date(6, 1, datetime.date.today().year - 21)
    bag = Bag()

    # Extract dates from the user and place them in the bag.
    date = promptAndExtractDate()
    while date is not None:
        bag.add(date)
        date = promptAndExtractDate()

    # Iterate over the bag and check the age.
    for date in bag:
        if date <= bornBefore:
            print("Is at least 21 years of age: ", date)


if __name__ == '__main__':
    main()
