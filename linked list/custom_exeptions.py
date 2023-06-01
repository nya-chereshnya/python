
class IndexOutOfBoundError(Exception):
    def __init__(self, index):
        self.index = index
        super().__init__(f"Index {index} is out of bounds")


class EmptyLinkedListError(Exception):
    def __init__(self):
        super().__init__(f"Cannot remove the head of an empty linked list")


class ElementNotFoundError(Exception):
    def __init__(self, data):
        self.data = data
        super().__init__(f"Element {data} not found")
