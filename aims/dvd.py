"""DVD model used by the AIMS-mini exercises."""

from decimal import Decimal, InvalidOperation


class DigitalVideoDisc:
    """A simple DVD with a title, category and non-negative selling cost."""

    def __init__(self, title: str, category: str = "General", cost=0):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string")
        if not isinstance(category, str) or not category.strip():
            raise ValueError("category must be a non-empty string")
        try:
            amount = Decimal(str(cost))
        except (InvalidOperation, ValueError):
            raise ValueError("cost must be a valid number") from None
        if amount < 0:
            raise ValueError("cost must not be negative")
        self.title = title.strip()
        self.category = category.strip()
        self.cost = amount

    def __repr__(self):
        return (f"DigitalVideoDisc(title={self.title!r}, "
                f"category={self.category!r}, cost={str(self.cost)!r})")