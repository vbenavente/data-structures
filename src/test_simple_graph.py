# -*- coding: utf-8 -*-
"""File tests our simple graph data structure."""
from __future__ import unicode_literals
import pytest

TEST_SG_DATA = [
    ("node_a", [])
]


def test_sg_init():
    """Ensure init returns a valid dictionary at self.graph."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    assert test_sg.graph == {}


def test_sg_nodes():
    """Ensure nodes returns a correct list of nodes in graph."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_node = test_sg.nodes()
    assert test_node == []


def test_sg_edges_empty_graph():
    """Ensure edges returns a correct list of edges in graph."""
    from simple_graph import SimpleGraph
    test_edge = SimpleGraph().edges()
    assert test_edge == []


def test_sg_edges():
    """Ensure edges returns correct list of edges in graph."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_edge("node_a", "node_b")
    assert test_sg.edges() == [("node_a", "node_b")]


@pytest.mark.parametrize('data, result', TEST_SG_DATA)
def test_sg_add_node(data, result):
    """Ensure new node is added to the graph."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_node(data)
    assert test_sg.graph[data] == result


def test_sg_add_node_error():
    """Ensure duplicate node raises IndexError."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_node("node_a")
    with pytest.raises(IndexError) as message:
        test_sg.add_node("node_a")
    assert "That node already exists dumbo." in str(message)


def test_sg_add_edge():
    """Ensure new edge is added to the graph."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_edge("node_a", "node_b")
    assert test_sg.graph["node_a"] == [("node_b", 1)]


def test_sg_del_node():
    """Ensure correct node is deleted, and all its edges are removed."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_edge("a", "c")
    test_sg.add_edge("b", "c")
    test_sg.add_edge("c", "b")
    test_sg.del_node("c")
    assert "c" not in test_sg.edges()


def test_sg_del_node_error():
    """Ensure del_node throws IndexError if called with node not in graph."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    with pytest.raises(IndexError) as message:
        test_sg.del_node("node_a")
    assert "That node is not in the graph." in str(message)


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
