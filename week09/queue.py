from __future__ import annotations
from enhanced_linked_list import EnhancedLinkedList


class Queue(EnhancedLinkedList):

    def enqueue(self, Node) -> None:
        self.add(Node)

    def dequeue(self) -> Node | None:
        node_to_return = self.__head
        if node_to_return is not None:
            self.__head = self.__head.get_next()
            self.__size -= 1
            if self.__size == 0:
                self.__tail = None
        return node_to_return
        
