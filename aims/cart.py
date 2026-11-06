"""Shopping cart operations for AIMS-mini."""

from .dvd import DigitalVideoDisc

MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd: DigitalVideoDisc) -> bool:
        """Add a DVD. Return False when the cart already contains 20 DVDs."""
        if not isinstance(dvd, DigitalVideoDisc):
            raise TypeError("dvd must be a DigitalVideoDisc")
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        return True

    def remove_dvd(self, dvd: DigitalVideoDisc) -> bool:
        try:
            self.items.remove(dvd)
            return True
        except ValueError:
            return False

    def total_cost(self) -> float:
        return float(sum((dvd.cost for dvd in self.items), start=0))

    def total_cost_with_discount(self, percent: float) -> float:
        """Return the remaining total for a percentage, including fractional values."""
        if not isinstance(percent, (int, float)) or not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")
        total = sum((dvd.cost for dvd in self.items), start=0)
        return float(total * (100 - percent) / 100)

    def sort_by_title(self):
        self.items.sort(key=lambda dvd: dvd.title.casefold())
        return list(self.items)

    def sort_by_cost(self):
        self.items.sort(key=lambda dvd: (dvd.cost, dvd.title.casefold()))
        return list(self.items)

    def print_cart(self) -> str:
        if not self.items:
            output = "The cart is empty"
        else:
            lines = ["***********************CART***********************"]
            lines.extend(
            f"{index}. {dvd.title} - {dvd.category} - {dvd.cost:.2f} $"
            for index, dvd in enumerate(self.items, start=1))
            lines.append(f"Total cost: {self.total_cost():.2f} $")
            lines.append("***************************************************")
            output = "\n".join(lines)
        print(output)
        return output


def sort_by_title(items):
    """Return a new list sorted by DVD title (case-insensitive)."""
    return sorted(items, key=lambda dvd: dvd.title.casefold())


def sort_by_cost(items):
    """Return a new list sorted by cost, then title."""
    return sorted(items, key=lambda dvd: (dvd.cost, dvd.title.casefold()))
