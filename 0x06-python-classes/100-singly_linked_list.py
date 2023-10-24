#!/usr/bin/python3

""" Defining a class Node that creates a singly
linked list """


class Node:
    """ A node of a singly linked list """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" Defining a class SinglyLinkedList that is a
singly linked list """


class SinglyLinkedList:
    """ A singly linked list of nodes """

    def __init__(self):
        self.__head = None

    def __str__(self):
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node and value >= current.next_node.data:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
