"""A consumer credit card class sample."""


class CreditCard:

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance. The initial balance is zero.

        :param customer:    The name of the customer (e.g. `John Bowman`).
        :param bank:        The name of the bank (e.g. `California Savings`).
        :param acnt:        The account identifier (e.g. (e.g. `5391 0375 9387 5309`).
        :param limit:       Credit limit (measured in dollars)
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


class PredatoryCreditCard(CreditCard):
    """An extension to :class:`CreditCard` that compounds interest and fees."""

    def __int__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card transfer with initial zero balance.

        :param customer:    The name of the customer (e.g. `John Bowman`).
        :param bank:        The name of the bank (e.g. `California Savings`).
        :param acnt:        The account identifier (e.g. `5391 0375 9387 5309`).
        :param limit:       Credit card limit (measured in USD).
        :param apr:         Annual percentage rate (e.g., 0.0825 for 8.25% APR).
        """
        super().__init__(customer, bank, acnt, limit)   # Call constructor.
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        :returns: True if charge was processed. False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)   # Call inherited method.
        if not success:
            self._balance += 5            # Assess penalty.
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
