from rest_framework.pagination import CursorPagination


class EventsPagination(CursorPagination):
    """
    Пагинатор для EventModel
    """

    def __init__(self, ordering="event_time", page_size: int = 10) -> None:
        self.ordering = ordering
        self.page_size = page_size
