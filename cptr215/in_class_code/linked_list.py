"""Linked List (LL)
A linked list is one of:
- empty
- a cell which has a data item and a linked list
"""

from abc import ABC, abstractmethod


class LL(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: 'LL') -> 'LL':
        pass

    @abstractmethod
    def reversed(self) -> 'LL':
        pass

    @abstractmethod
    def __getitem__(self, pos: int) -> int:
        pass

    @abstractmethod
    def count(self, item: int) -> int:
        pass


class Empty(LL):
    def __repr__(self) -> str:
        return "Empty()"

    def __str__(self) -> str:
        return ""

    def __len__(self) -> int:
        return 0

    def sum(self) -> int:
        return 0

    def __contains__(self, item: int) -> bool:
        return False

    def evens(self) -> LL:
        return self  # could also say Empty()

    def __add__(self, other):
        return other

    def reversed(self):
        return self

    def __getitem__(self, pos: int) -> int:
        return self.data if pos == 0 else self.rest[pos - 1]

    def count(self, item: int) -> int:
        return 0


class Cell(LL):
    def __init__(self, data: int, rest: LL):
        self.data = data
        self.rest = rest

    def __repr__(self) -> str:
        return f"Cell({self.data!r}, {self.rest!r})"

    def __str__(self) -> str:
        return f"{self.data} {self.rest}"

    def __len__(self) -> int:
        return 1 + len(self.rest)

    def sum(self) -> int:
        # return ... self.data ... self.rest.??? ...
        return self.data + self.rest.sum()

    def __contains__(self, item) -> bool:
        return self.data == item or item in self.rest

    def evens(self) -> LL:
        if self.data % 2 == 0:
            return Cell(self.data, self.rest.evens())
        else:
            return self.rest.evens()

    def __add__(self, other: LL):
        return Cell(self.data, self.rest + other)  # self.rest.__add__(other)

    def reversed(self):
        return self.rest.reversed() + Cell(self.data, Empty())

    def __getitem__(self, pos: int) -> int:
        return self.data if pos == 0 else self.rest[pos - 1]

    def count(self, item: int) -> int:
        return self.rest.count(item) + (1 if self.data == item else 0)


# Some examples
short_list = Cell(0, Empty())
my_list = Cell(3, Cell(6, Cell(8, Empty())))
print(repr(my_list))
print(my_list)
print(len(my_list))
print(my_list.sum())
print(1 in my_list)
print(my_list.evens())
print(short_list + my_list)  # Cell(0, Cell(3, Cell(6, Cell(8, Empty()))))
print(my_list + short_list)  # Cell(3, Cell(6, Cell(8, Cell(0, Empty()))))
print(my_list.reversed())  # Cell(8, Cell(6, Cell(3, Empty())))
"""
>>> my_list[1]
6
>>> my_list[0]
8
>>> my_list.count(2)
0
>>> my_list[3]
ERROR
>>> my_list.zip(Cell(2, Cell(4, Cell(6, Empty()))))
8 2 6 4 3 6
"""
