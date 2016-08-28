# -*- coding: utf-8 -*-
"""File tests our simple graph data structure."""
from __future__ import unicode_literals
import pytest


def test_sg_init():
    """Ensure init returns a valid list at self.graph."""


def test_sg_nodes():
    """Ensure nodes returns a correct list of nodes in graph."""


def test_sg_edges():
    """Ensure edges returns a correct list of edges in graph."""


def test_sg_add_node():
    """Ensure new node is added to the graph."""


def test_sg_add_node_error():
    """Ensure duplicate node raises IndexError."""


def test_sg_add_edge():
    """Ensure new edge is added to the graph."""


def test_sg_del_node():
    """Ensure correct node is deleted, and all its edges are removed."""


def test_sg_del_node_error():
    """Ensure del_node throws IndexError if called with node not in graph."""


def test_sg_del_edge():
    """Ensure supplied edge is deleted from appropriate node."""


def test_sg_del_edge_error():
    """Ensure del_edge throws IndexError if called with node not in graph."""


def test_sg_has_node_true():
    """Ensure has_node returns true when called with node in graph."""


def test_sg_has_node_false():
    """Ensure has_node returns false when called with node not in graph."""


def test_sg_neighbors():
    """Ensure neighbors for node that exists are returned."""


def test_sg_neighbors_error():
    """Ensure error is raised if node does not exist in graph."""


def test_sg_adjacent_true():
    """Ensure adjacent returns true if a and b share an edge."""


def test_sg_adjacent_false():
    """Ensure adjacent returns false if a and b don't share an edge."""


def test_sg_adjace_error():
    """Ensure adjacent raises an error if either node doesn't exist."""
