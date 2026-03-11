from node import Node 

class LinkedList:

    """A simple linked list data structure."""

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __str__(self):
        result = ""
        current = self.__head
        while current != None:
            result += str(current) + " "
            current = current.get_next()
        return result
    
    def get_size(self):
        return self.__size
    
    def add(self, value):
        new_node = Node(value)
        if self.__head == None:
            self.__head = new_node
        else:
            self.__tail.set_next(new_node)
        self.__tail = new_node
        self.__size += 1

if __name__ == "__main__":
    test = LinkedList()
    test.add(1)
    test.add(2)
    test.add(3)
    print(test)