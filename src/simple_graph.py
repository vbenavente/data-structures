# -*- coding: utf-8 -*-
"""File implements a simple graph data structure."""
from __future__ import unicode_literals


class SimpleGraph(object):
    """Simple_graph implements a simple graph data structure.

    We support 1 way edges and lots of methods described below.

    Sample structure illustrates the concept.  Nodes a, b, c and d exist
    and could have any valid python value.  The sub-list contains
    edges for every node.  For instance, node_a shares an edge with
    node_b, but node_b has no edge with node_a.  Node_b has no edges
    of it's own, but node_a, c and d are all neighbors of b.

    Graph:  {
                "node_a": [node_b],
                "node_b": [],
                "node_c": [node_b],
                "node_d": [node_a, node_b, node_c],
            }
    """

    def __init__(self):
        """Initialize an empty simple_graph class instance.

        We don't accept a value here, you must start with an empty graph
        and add data manually via public methods."""
        self.graph = {}

    def nodes(self):
        """Returns a list of all nodes in the graph."""
        node_list = []
        for i in self.graph:
            node_list.append(self.graph[i])
        return node_list

    def edges(self):
        """Returns a list of all edges in the graph."""
        edge_list = []
        for i in self.graph:
            for j in self.graph[i]:
                edge_list.append(self.graph[i], self.graph[i][j])
        return edge_list

    def add_node(self, node):
        """Adds a new node to the graph."""
        if node in self.graph:
            raise IndexError("That node already exists dumbo.")
        else:
            self.graph[node] = []

    def add_edge(self, node_1, node_2):
        """Adds an edge between node_1 and node_2.

        If node_1 or node_2 are not present, function adds them to the graph
        first.  Edges are single direction only."""
        if node_1 not in self.graph:
            self.add_node(node_1)
        if node_2 not in self.graph:
            self.add_node(node_2)
        self.graph[node_1].append(node_2)

    def del_node(self, node):
        """Deletes a node from the graph.

        Removes all existing edges pointing to node before deleting node.
        Throws a IndexError if node specified does not exist."""

    def del_edge(self, node_1, node_2):
        """Deletes and edge between node_1 and node_2.

        Only removes the edge in the direction node_1 -->  node_2.
        Raises a IndexError if that edge does not exist in graph."""

    def has_node(self, node):
        """Returns True if node exists in the graph, otherwise False."""

    def neighbors(self, node):
        """Returns a list of all nodes connected to node by edges.

        Raises an IndexError if node does not exist in graph."""

    def adjacent(self, node_1, node_2):
        """Returns True if node_1 and node_2 share an edge, otherewise False.

        Raises an IndexError if either node does not exist in graph."""
