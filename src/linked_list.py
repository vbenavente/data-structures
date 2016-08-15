# -*- coding: utf-8 -*-
class Node(object):
    """This sets our Node class"""
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None


    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        elif self.next_node is None:
            self.next_node = self.new_node
        else:
            self.next_node = None

    def remove(data):
        pass

    def search(data):
        pass

    def display():
        pass

    def pop():
        pass
