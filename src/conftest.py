# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import namedtuple
import pytest


"""DLL Fixtures"""

TEST_DLL_INIT_DATA = [
    ("encyclopedia",),
    "taco",
    "zebra",
    [1, 2, 3],
]

TEST_DLL_INIT_DATA2 = [
    ("booksarecool",),
    "rhino",
    [1, 99, 7],
]


@pytest.fixture(scope="function")
def dll_initial_1():
    from dll import DoublyLinkedList
    temp = DoublyLinkedList(TEST_DLL_INIT_DATA)
    return temp


@pytest.fixture(scope="function")
def dll_initial_2():
    from dll import DoublyLinkedList
    temp = DoublyLinkedList(TEST_DLL_INIT_DATA2)
    return temp


"""Heap Fixtures"""

Heap_Fix = namedtuple("Heap_Fix", ("data",
                                   "result",
                                   "output",
                                   "input",
                                   "instance",
                                   "expected",
                                   "initial",
                                   "childs",
                                   ))
Heap_Fix.__new__.__defaults__ = (None,) * len(Heap_Fix._fields)
# the above line sourced from:
# http://stackoverflow.com/questions/11351032/named-tuple-and-optional-keyword-arguments

HEAP_FIX_ONE_DATA = [
    ((1, ), 1, (None, None)),
    ((1, 2), 2, (None, None)),
    ((2, 1), 2, (None, None)),
    ((45, 87, 3, 27), 4, (None, None)),
    ((7, 5, 9, 345, 43, 873), 6, (None, None)),
    ((8, 7, 6, 5, 4, 3, 2, 1), 8, (7, None)),
    ((1, 2, 3, 4, 5, 6, 7, 8, 9), 9, (7, 8)),
    ((34, 0, 77, 95, 21, 8009, 788324), 3, (None, None)),
    (list(range(64, 200)), 0, (7, 8)),
    (list(range(-15, 50)), 65, (7, 8))
]


@pytest.fixture(scope="function")
def heap_fix_empty():
    """Return a new test instance of Heap class."""
    from heap import Heap
    instance = Heap()
    return instance


@pytest.fixture(scope="function", params=HEAP_FIX_ONE_DATA)
def heap_fix_one(request):
    """Return a new test instance of Heap class."""
    from heap import Heap
    instance = Heap(request.param[0])
    result = sorted(request.param[0])[0]
    expected = request.param[1]
    initial = sorted(request.param[0])
    childs = request.param[2]
    named_tuple = Heap_Fix(instance=instance,
                           result=result,
                           expected=expected,
                           initial=initial,
                           childs=childs
                           )
    return named_tuple


"""Priority Queue Fixtures"""


Priorityq_Fix = namedtuple("Priorityq_Fix", ("instance",
                                             "pq_insert",
                                             "pq_insert_count"))

Priorityq_Fix.__new__.__defaults__ = (None,) * len(Priorityq_Fix._fields)
# the above line sourced from:
# http://stackoverflow.com/questions/11351032/named-tuple-and-optional-keyword-arguments

TEST_PQ_DATA = [
    [[(1, "taco")], (3, "airplane")],
    [[(1, "taco"), (88, "dolorean")], (2, "hotdog")],
    [[(3, ["texmex", "hiyall", "yes"]), (3, 8), (3, {"key": "value"})], (4, "baseball")],
    [[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7")], (1, "pitcher")],
]


@pytest.fixture(scope="function", params=TEST_PQ_DATA)
def pq_fix_one(request):
    """Return a new test instance of priority queue class."""
    from priorityq import Priorityq
    instance = Priorityq(request.param[0])
    pq_insert = request.param[1]
    pq_insert_count = len(request.param[0]) + 1
    named_tuple = Priorityq_Fix(instance=instance,
                                pq_insert=pq_insert,
                                pq_insert_count=pq_insert_count)
    return named_tuple


"""Graph Traversal Fixtures."""


@pytest.fixture(scope="function")
def graph_test_case_one():
    """Return a test instance of graph traversal."""
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_edge("a", "b")
    instance.add_edge("a", "c")
    instance.add_edge("c", "d")
    instance.add_edge("c", "e")
    instance.add_edge("e", "h")
    instance.add_edge("e", "g")
    instance.add_edge("e", "f")
    return instance


@pytest.fixture(scope="function")
def graph_test_case_two():
    """Return a test instance for graph traversal."""
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_edge("a", "d")
    instance.add_edge("a", "c")
    instance.add_edge("a", "b")
    instance.add_edge("d", "g")
    instance.add_edge("g", "h")
    instance.add_edge("h", "j")
    instance.add_edge("h", "i")
    instance.add_edge("b", "e")
    instance.add_edge("e", "f")
    return instance


@pytest.fixture(scope="function")
def graph_test_case_three():
    """Return a test instance that is cyclic for graph traversal."""
    from simple_graph import SimpleGraph
    instance = SimpleGraph()
    instance.add_edge("a", "b")
    instance.add_edge("b", "c")
    instance.add_edge("c", "d")
    instance.add_edge("c", "e")
    instance.add_edge("d", "h")
    instance.add_edge("h", "d")
    instance.add_edge("e", "f")
    instance.add_edge("f", "g")
    instance.add_edge("g", "a")
    instance.add_edge("g", "i")
    instance.add_edge("i", "j")
    return instance
