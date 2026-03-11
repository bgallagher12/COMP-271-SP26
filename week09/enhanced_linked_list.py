from __future__ import annotations
from linked_list import LinkedList


class EnhancedLinkedList(LinkedList):

    def __init__(self):
        super().__init__()

    def is_empty(self) -> bool:
        return self.__size == 0

    def size(self) -> int:
        return self.__size
    
    def peek(self) -> Node | None:
        return None if self.is_empty() else self.__head