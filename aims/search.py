"""Search helpers for DVD collections."""


def search_by_title(items, keyword):
    normalized_keyword = keyword.strip().casefold()

    if not normalized_keyword:
        return []

    return [
        dvd for dvd in items
        if normalized_keyword in dvd.title.casefold()
    ]