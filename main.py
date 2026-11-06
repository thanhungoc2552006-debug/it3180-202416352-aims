"""Small command-line demonstration of AIMS-mini."""

from aims import Cart, DigitalVideoDisc, __version__
from aims.search import search_by_title


def build_demo_cart():
    cart = Cart()
    # The sample total is deliberately 63.89 $, as specified in the lab guide.
    cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", "19.95"))
    cart.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", "24.95"))
    cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", "18.99"))
    return cart


def main():
    cart = build_demo_cart()
    print(f"AIMS-mini v{__version__}")
    print(f"Total cost: {cart.total_cost():.2f} $")
    matches = search_by_title(cart.items, "lion")
    print("Search 'lion': " + ", ".join(dvd.title for dvd in matches))


if __name__ == "__main__":
    main()