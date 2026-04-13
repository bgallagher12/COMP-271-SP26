class Node:

    """A node in a linked list."""
    
    def __init__(self, value):
        """Initializes a node with the given value. A 
        new node always points to None for its next field."""
        self.__value = value
        self.__next = None

    def __str__(self):
        return str(self.__value)

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next

    def has_next(self):
        return self.__next != None
    