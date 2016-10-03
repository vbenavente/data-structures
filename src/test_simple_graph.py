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
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_edge("B", "c")
    test_sg.del_edge("B", "c")
    assert ("B", "c") not in test_sg.edges()


def test_sg_del_edge_error():
    """Ensure del_edge throws IndexError if called with node not in graph."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_edge("a", "b")
    with pytest.raises(IndexError) as message:
        test_sg.del_edge("c", "b")
    assert "That edge is not in the graph." in str(message)


def test_sg_has_node_true():
    """Ensure has_node returns true when called with node in graph."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_node("a")
    assert test_sg.has_node("a") is True


def test_sg_has_node_false():
    """Ensure has_node returns false when called with node not in graph."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    assert test_sg.has_node("a") is False


def test_sg_neighbors():
    """Ensure neighbors for node that exists are returned."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_edge("b", "z")
    test_sg.add_edge("b", "c")
    assert test_sg.neighbors("b") == ["z", "c"]


def test_sg_neighbors_error():
    """Ensure error is raised if node does not exist in graph."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    with pytest.raises(IndexError) as message:
        test_sg.neighbors("a")
    assert "That node is not in the graph." in str(message)


def test_sg_adjacent_true():
    """Ensure adjacent returns true if a and b share an edge."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_edge("a", "b")
    assert test_sg.adjacent("a", "b") is True


def test_sg_adjacent_false():
    """Ensure adjacent returns false if a and b don't share an edge."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_node("a")
    test_sg.add_node("b")
    assert test_sg.adjacent("a", "b") is False


def test_sg_adjace_error_one():
    """Ensure adjacent raises an error if either node doesn't exist."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_node("b")
    with pytest.raises(IndexError) as message:
        test_sg.adjacent("a", "b")
    assert "First argument is not in the graph." in str(message)


def test_sg_adjace_error_two():
    """Ensure adjacent raises an error if either node doesn't exist."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    test_sg.add_node("a")
    with pytest.raises(IndexError) as message:
        test_sg.adjacent("a", "b")
    assert "Second argument is not in the graph." in str(message)


def test_sg_depth_first_traversal_empty():
    """Ensure an empty result is handed back when called on empty graph."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    with pytest.raises(IndexError) as message:
        test_sg.depth_first_traversal("a")
    assert "That starting point is not in the graph." in str(message)


def test_sg_depth_first_traversal_case_one(graph_test_case_one):
    """Test depth-first against test case one."""
    test_graph_depth = graph_test_case_one.depth_first_traversal("a")
    assert test_graph_depth[1] == "b" or test_graph_depth[-1] == "b"


def test_sg_depth_first_traversal_case_two(graph_test_case_two):
    """Test depth-first against test case two."""
    test_graph_depth = graph_test_case_two.depth_first_traversal("a")
    assert test_graph_depth[1] == "c" or test_graph_depth[4] == "c" or test_graph_depth[-1] == "c" or test_graph_depth[6] == "c"


def test_sg_depth_first_traversal_case_three(graph_test_case_three):
    """Test depth-first against test case three, cyclic graph.

    Ensure traversal does not get stuck in endless loop."""
    test_graph_depth = graph_test_case_three.depth_first_traversal("a")
    assert test_graph_depth[9] == "j" or test_graph_depth[7] == "j"


def test_sg_breadth_first_traversal_empty():
    """Ensure an empty result is handed back when called on empty graph."""
    from simple_graph import SimpleGraph
    test_sg = SimpleGraph()
    with pytest.raises(IndexError) as message:
        test_sg.breadth_first_traversal("a")
    assert "That starting point is not in the graph." in str(message)


def test_sg_breadth_first_traversal_case_one(graph_test_case_one):
    """Test breadth-first against test case one."""
    test_graph_breadth = graph_test_case_one.breadth_first_traversal("a")
    assert test_graph_breadth[1] == "b" or test_graph_breadth[2] == "b"


def test_sg_breadth_first_traversal_case_two(graph_test_case_two):
    """Test breadth-first against test case two."""
    test_graph_breadth = graph_test_case_two.breadth_first_traversal("a")
    assert test_graph_breadth[1] == "b" or test_graph_breadth[2] == "b" or test_graph_breadth[3] == "b"


def test_sg_breadth_first_traversal_case_three(graph_test_case_three):
    """Test breadth-first against test case three, cyclic graph.

    Ensure traversal does not get stuck in endless loop."""
    test_graph_breadth = graph_test_case_three.breadth_first_traversal("a")
    assert test_graph_breadth[-1] == "j"


def test_sg_verify_edge_weights():
    """Verify that when edges are added to the graph with a specified weight
    they have that weight."""
    from simple_graph import SimpleGraph
    test_graph = SimpleGraph()
    test_graph.add_edge("a", "b", 7)
    assert test_graph.graph["a"][0][1] == 7
