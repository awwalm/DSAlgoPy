"""A consumer credit card class sample."""


class CreditCard:

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance. The initial balance is zero.

        :param customer:    The name of the customer (e.g. `John Bowman`).
        :type customer:     str
        :param bank:        The name of the bank (e.g. `California Savings`).
        :type bank:         str
        :param acnt:        The account identifier (e.g. (e.g. `5391 0375 9387 5309`).
        :type acnt:         str
        :param limit:       Credit limit (measured in dollars)
        :type limit:        double
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank's name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.

        :returns: ``True`` if charge was processed; ``False`` if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount
