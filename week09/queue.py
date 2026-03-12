from __future__ import annotations
from enhanced_linked_list import EnhancedLinkedList
from node import Node


class Queue(EnhancedLinkedList):

    def __init__(self):
        """Superfluous constructor, but it is here to show that we can
        extend the EnhancedLinkedList class."""
        super().__init__()

    def enqueue(self, Node) -> None:
        """Enqueueing is just adding to the end of the queue, which is
        the tail of the linked list. So we can just reuse the add method
        from the parent class."""
        self.add(Node)

    def dequeue(self) -> Node | None:
        """Dequeueing is removing from the front of the queue."""
        return self.remove(0)
    
    def peek(self) -> Node | None:
        """Returns the node at the front of the queue without removing it."""
        return self.inspect(0)


# Brutally naive testing
if __name__ == "__main__":
    test = Queue()
    test.enqueue(Node("LEO"))
    print(test.dequeue())
    print(test.dequeue())
