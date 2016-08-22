# -*- coding: utf-8 -*-
"""File tests our queue data structure."""
from __future__ import unicode_literals
import pytest
from queue import Queue

TEST_QUEUE_DATA = [
    [1, 2, 3, 4, 5],
    7,
    "zebra",
    {"whatup": "Vote For Pedro"},
    ("cup", "coffee", "pastry")
]

TEST_QUEUE_MUCHO_DATA = (("a b c ") * 200)


def test_queue_init():
    """Test that list initialized successfully."""
    assert Queue(TEST_QUEUE_DATA).dll.head.data == ("cup", "coffee", "pastry")


def test_queue_enqueue():
    """Test that enqueue'd data is added to the head of the queue."""
    test_queue = Queue(TEST_QUEUE_DATA)
    test_queue.enqueue("stripes")
    assert test_queue.dll.head.data == "stripes"


def test_queue_dequeue():
    """Test dequeue'd node is no longer in queue."""
    test_queue = Queue(TEST_QUEUE_DATA)
    assert test_queue.dequeue() == [1, 2, 3, 4, 5]


def test_queue_dequeue_empty():
    """Test dequeue on empty list raises error."""
    test_case = Queue()
    with pytest.raises(IndexError) as message:
        test_case.dequeue()
    assert "This queue is empty." in str(message)


def test_queue_peek():
    """Test peek returns the next value in the queue."""
    test_queue = Queue(TEST_QUEUE_DATA)
    assert test_queue.peek() == [1, 2, 3, 4, 5]


def test_queue_peek_none():
    """Test peek returns none if queue is empty."""
    test_queue = Queue()
    assert test_queue.peek() is None


def test_queue_size():
    """Test size returns size of queue."""
    test_queue = Queue(TEST_QUEUE_DATA)
    assert test_queue.size() == 5


def test_queue_size_empty():
    """Test empty queue has size 0."""
    test_queue = Queue()
    assert test_queue.size() == 0


def test_queue_size_mucho():
    """Test that list initialized with mucho data successfully."""
    assert Queue(TEST_QUEUE_MUCHO_DATA).size() == 1200
