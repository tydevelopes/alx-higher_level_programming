#!/usr/bin/python3
"""Module defines a singly linked list data structure"""


class Node:
    """Defines a node class"""

    @property
    def data(self):
        """Return private data property"""

        return self.__data

    @data.setter
    def data(self, value):
        """Set data property"""

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return private next_node property"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set private next_node property"""

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __init__(self, data, next_node=None):
        """Initializes a class object"""

        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """Defined a singly linked list"""

    def __init__(self):
        """Initializes a singly linked list object"""

        self.__head = None

    def __str__(self):
        """Prints all data in a list"""
        current_node = self.__head
        string = ""
        empty = ""
        newline = "\n"
        i = 0

        while current_node is not None:
            string += f"{empty if i == 0 else newline}{current_node.data}"
            current_node = current_node.next_node
            i += 1

        return string

    def sorted_insert(self, value):
        """insert node in a sorted list"""

        current_node = self.__head
        previous_node = None
        position = 0
        temp_node = Node(value)

        while current_node is not None and value > current_node.data:
            previous_node = current_node
            current_node = current_node.next_node
            position += 1

        if current_node is None and position == 0:
            self.__head = temp_node
        elif previous_node is None and position == 0:
            temp_node.next_node = current_node
            self.__head = temp_node
        else:
            previous_node.next_node = temp_node
            temp_node.next_node = current_node
