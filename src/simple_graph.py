# -*- coding: utf-8 -*-
"""File implements a simple graph data structure."""
from __future__ import unicode_literals


class SimpleGraph(object):
    """Simple_graph implements a simple graph data structure.

    We support 1 way edges and lots of methods described below."""

    def __init__(self):
        """Initialize a simple_graph class instance."""
        pass

    def nodes(self):
        """Returns a list of all nodes in the graph."""

    def edges(self):
        """Returns a list of all edges in the graph."""

    def add_node(self, node):
        """Adds a new node to the graph."""

    def add_edge(self, node_1, node_2):
        """Adds an edge between node_1 and node_2.

        If node_1 or node_2 are not present, function adds them to the graph
        first.  Edges are single direction only."""

    def del_node(self, node):
        """Deletes a node from the graph.

        Removes all existing edges pointing to node before deleting node.
        Throws a IndexError if node specified does not exist."""

    def del_edge(self, node_1, node_2):
        """Deletes and edge between node_1 and node_2.

        Raises a IndexError if that edge does not exist in graph."""

    def has_node(self, node):
        """Returns True if node exists in the graph, otherwise False."""

    def neighbors(self, node):
        """Returns a list of all nodes connected to node by edges.

        Raises an IndexError if node does not exist in graph."""

    def adjacent(self, node_1, node_2):
        """Returns True if node_1 and node_2 share an edge, otherewise False.

        Raises an IndexError if either node does not exist in graph."""
