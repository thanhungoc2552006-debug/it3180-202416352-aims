"""Search helpers for DVD collections."""


def search_by_category(items, category):
    normalized = category.strip().casefold()
    if not normalized:
        return []
    return [dvd for dvd in items if dvd.category.casefold() == normalized]


def search_by_title(items, keyword):
    from unicodedata import normalize

    normalized_keyword = normalize("NFC", keyword.strip()).casefold()

    if not normalized_keyword:
        return []

    return [
        dvd for dvd in items
        if normalized_keyword in normalize("NFC", dvd.title).casefold()
    ]
