from __future__ import annotations
from linked_list import LinkedList
from node import Node


class EnhancedLinkedList(LinkedList):

    def __init__(self):
        """Superfluous constructor, but it is here to show that we can 
        extend the LinkedList class."""
        super().__init__()

    def is_empty(self) -> bool:
        """Returns True if the linked list is empty, False otherwise."""
        return self._size == 0

    def size(self) -> int:
        """Returns the number of nodes in the linked list."""
        return self._size
    
    def inspect(self, i:int) -> Node:
        """Returns the node at index i in the linked list."""
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")
        current = self._head
        for _ in range(i):
            current = current.next
        return current
    
    def remove(self, i:int) -> Node | None:
        """Removes and returns the node at index i in the linked list."""
        if i < 0 or i >= self._size:
            raise IndexError("Index out of bounds")
        if i == 0:
            return self.remove_first()
        current = self._head
        for _ in range(i - 1):
            current = current.next
        removed_node = current.next
        current.next = removed_node.next
        self._size -= 1
        return removed_node 