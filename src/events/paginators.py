from rest_framework.pagination import CursorPagination


class EventsPagination(CursorPagination):
    def __init__(self, ordering="date", page_size: int = 10) -> None:
        self.ordering = ordering
        self.page_size = page_size
