from __future__ import annotations
from enhanced_linked_list import EnhancedLinkedList
from node import Node

class Stack(EnhancedLinkedList):

    def __init__(self):
        """Superfluous constructor, but it is here to show that we can
        extend the EnhancedLinkedList class."""
        super().__init__()

    def push(self, new_node: Node) -> None:
        """Pushing is just adding to the top of the stack, which is
        the head of the linked list. There is no method to do this
        in the parent class, so we have to implement it ourselves."""
        # Have the new node point to the current head
        new_node.set_next(self._head)
        # Update the head to be the new node
        self._head = new_node
        # If the stack was previously empty, we also need to update the tail
        if self._size == 0:
            self._tail = new_node
        # Finally, update the size of the stack
        self._size += 1

    def pop(self) -> Node | None:
        """Popping is removing from the top of the stack."""
        return self.remove(0)
    
    def peek(self) -> Node | None:
        """Returns the node at the top of the stack without removing it."""
        return self.inspect(0)