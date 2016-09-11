"""File tests our priority queue data structure implementation."""
from __future__ import unicode_literals
import pytest


def test_pq_init(pq_fix_one):
    """Ensure init method of Priority Queue class works correctly."""
    assert len(pq_fix_one.instance.heap.heap[0]) == 3


def test_qp_init_none():
    """Ensure init method works with None input."""
    from priorityq import Priorityq
    test_case = Priorityq()
    assert isinstance(test_case, Priorityq)


def test_pq_init_iterable_err():
    """Ensure index error raised if a non iterable item is in the list."""
    from priorityq import Priorityq
    with pytest.raises(IndexError) as message:
        Priorityq(1)
    assert "Enter a list of tuples, each with 2 values." in str(message)


def test_pq_init_type_tuple():
    """Ensure items in list are all tuples."""
    from priorityq import Priorityq
    with pytest.raises(IndexError) as message:
        Priorityq([1, 2])
    assert "Enter a list of tuples, each with 2 values." in str(message)


def test_pq_init_first_tupval():
    """Ensure first value in tuple is a integer."""
    from priorityq import Priorityq
    with pytest.raises(IndexError) as message:
        Priorityq([(1, 2), ("taco", 3)])
    assert "First value in tuple must be an integer." in str(message)


def test_pq_insert(pq_fix_one):
    """Ensure insert adds tuple to priority queue."""
    pq_fix_one.instance.insert(pq_fix_one.pq_insert)
    assert (pq_fix_one.pq_insert[0], pq_fix_one.pq_insert_count, pq_fix_one.pq_insert[1]) in pq_fix_one.instance.heap.heap


def test_pq_insert_error_tuple(pq_fix_one):
    """Ensure items to be added is a tuple."""
    with pytest.raises(IndexError) as message:
        pq_fix_one.instance.insert(17)
    assert "Enter a tuple with 2 values." in str(message)


def test_pq_insert_error_tupval(pq_fix_one):
    """Ensure first value in tuple is an integer."""
    with pytest.raises(TypeError) as message:
        pq_fix_one.instance.insert(("frog", "yellow"))
    assert "First value in tuple must be an integer." in str(message)


def test_pq_pop(pq_fix_one):
    """Ensure pop removes the top priority of the queue."""
    priority = sorted(pq_fix_one.instance.heap.heap)
    assert pq_fix_one.instance.pop() == priority[0][2]


def test_pq_peek(pq_fix_one):
    """Show highest priority value in list without removing it."""
    length_priority = len(sorted(pq_fix_one.instance.heap.heap))
    prior_peek_list = pq_fix_one.instance.heap.heap
    pq_fix_one.instance.peek()
    assert length_priority == len(prior_peek_list)


def test_pq_peek_empty():
    """Ensure error is raised when peek at empty pqueue."""
    from priorityq import Priorityq
    test_case = Priorityq([(1, 2)])
    test_case.pop()
    with pytest.raises(IndexError) as message:
        test_case.peek()
    assert "You can't peek at an empty priority queue." in str(message)
