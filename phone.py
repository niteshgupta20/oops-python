from item import Item


# INHERITANCE
class Phone(Item):
    # all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal 0"

        # assign to self object
        self.broken_phones = broken_phones

        # Actions to execute
        # Phone.all.append(self)
