"""Drafts for the Sales Store program."""
from RDNecaise.Chapter2.array import Array
from RDNecaise.Chapter3.array import MultiArray


class Store(MultiArray):
    """Creates a store object meant to be modelled as a 3-D array: ``[stores, items, months]``."""

    def __init__(self, *dimensions):
        assert len(dimensions) == 3, "Exactly 3 dimensions must be specified."
        assert 0 < dimensions[2] < 13, "Month must be in the range of 1-12."
        super().__init__(*dimensions)

    def totalSalesByStore(self: MultiArray, store):
        """Compute the total sales of all items for all months in a given store."""
        s = store - 1                         # Subtract 1 from the store number [index = n-1].
        total = 0.0                           # Accumulate the total sales for the given store.
        for i in range(self.length(2)):       # Iterate over the items.
            for m in range(self.length(3)):   # Iterate over each month of the i item.
                total += self[s, i, m]
        return total

    def totalSalesByMonth(self, month):
        """Compute the total sales of all items in all stores for a given month."""
        m = month - 1                         # The months number must be offset by 1.
        total = 0.0                           # Accumulate the total sales for the given month.
        for s in range(self.length(1)):       # Iterate over each store.
            for i in range(self.length(2)):   # Iterate over each item of the s store.
                total += self[s, i, m]
        return total

    def totalSalesByItem(self, item):
        """Compute the total sales of a single item in all stores over all months."""
        i = item - 1                          # The item number must be offset by 1.
        total = 0                             # Accumulate the total sales for the given month.
        for s in range(self.length(1)):       # Iterate over each store.
            for m in range(self.length(3)):   # Iterate over each month of the s store.
                total += self[s, i, m]
        return total

    def totalSalesPerMonth(self, store):
        """Compute the total sales per month for a given store.
        A 1-D array is returned that contains totals for each month.
        """
        s = store - 1                         # The store number must be offset by 1.
        totals = Array(12)                    # The totals will be returned in a 1-D array.
        for m in range(self.length(3)):       # Iterate over the sales of each month.
            subtotal = 0.0
            for i in range(self.length(2)):   # Iterate over the sales of each item sold during the m month.
                subtotal += self[s, i, m]
            totals[m] = subtotal              # Store the result in the month of the totals array.
        return totals
