"""Drafts for the Sales Store program."""

from RDNecaise.Chapter3.array import MultiArray


class Store(MultiArray):
    """Creates a store object meant to be modelled as a 3-D array: ``[stores, items, months]``."""

    def __init__(self, *dimensions):
        assert len(dimensions) == 3, "Exactly 3 dimensions must be specified."
        assert 0 < dimensions[2] < 13, "Month must be in the range of 1-12."
        super().__init__(*dimensions)

    def totalSalesByStore(self: MultiArray, store):
        """Compute the total sales of all items for all months in a given store."""
        # Subtract 1 from the store number since the array indices are 1 less than the given store.
        s = store - 1
        # Accumulate the total sales for the given store.
        total = 0.0
        # Iterate over the items (recall that the second dimension correlates with the ITEMS data).
        for i in range(self.length(2)):
            # Iterate over each month of the i item (third dimension correlates to MONTHS).
            for m in range(self.length(3)):
                total += self[s, i, m]
        return total

    def totalSalesByMonth(self, month):
        """Compute the total sales of all items in all stores for a given month."""
        # The months number must be offset by 1.
        m = month-1
        # Accumulate the total sales for the given month.
        total = 0.0
        # Iterate over each store.
        for s in range(self.length(1)):
            # Iterate over each item of the s store.
            for i in range(self.length(2)):
                total += self[s, i, m]
        return total
