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
    of it's own, but node_a, c and b are all neighbors of d.

    Graph:  {
                "node_a": [(node_b, 1)],
                "node_b": [],
                "node_c": [(node_b, 1)],
                "node_d": [(node_a, 1), (node_b, 1), (node_c, 1)],
            }
    """

    def __init__(self):
        """Initialize an empty simple_graph class instance.

        We don't accept a value here, you must start with an empty graph
        and add data manually via public methods."""
        self.graph = {}

    def nodes(self):
        """Returns a list of all nodes in the graph."""
        return list(self.graph.keys())

    def edges(self):
        """Returns a list of all edges in the graph."""
        edge_list = []
        for key in self.graph:
            for n, w in self.graph[key]:
                edge_list.append((key, n))
        return edge_list

    def add_node(self, node):
        """Adds a new node to the graph."""
        if node in self.graph:
            raise IndexError("That node already exists dumbo.")
        else:
            self.graph[node] = []

    def add_edge(self, node_1, node_2, weight=1):
        """Adds an edge between node_1 and node_2.

        If node_1 or node_2 are not present, function adds them to the graph
        first.  Edges are single direction only."""
        if node_1 not in self.graph:
            self.add_node(node_1)
        if node_2 not in self.graph:
            self.add_node(node_2)
        self.graph[node_1].append((node_2, weight))

    def del_node(self, node):
        """Deletes a node from the graph.

        Removes all existing edges pointing to node before deleting node.
        Throws a IndexError if node specified does not exist."""
        if node not in self.graph:
            raise IndexError("That node is not in the graph.")
        else:
            edge_list = self.edges()
            for n in edge_list:
                if n[1] == node:
                    val_list = self.graph[n[0]]
                    for val in val_list[:]:
                        val_list.remove(val)
            self.graph.pop(node)

    def del_edge(self, node_1, node_2):
        """Deletes and edge between node_1 and node_2.

        Only removes the edge in the direction node_1 -->  node_2.
        Raises a IndexError if that edge does not exist in graph."""
        edge_list = self.edges()
        tup = (node_1, node_2)
        if tup not in edge_list:
            raise IndexError("That edge is not in the graph.")
        else:
            val_to_remove = [val for idx, val in enumerate(self.graph[node_1]) if val[0] == node_2][0]
            self.graph[node_1].remove(val_to_remove)

    def has_node(self, node):
        """Returns True if node exists in the graph, otherwise False."""
        nodes = list(self.graph.keys())
        if node in nodes:
            return True
        else:
            return False

    def neighbors(self, node):
        """Returns a list of all nodes connected to node by edges.

        Raises an IndexError if node does not exist in graph."""
        neighbors = []
        try:
            for t in self.graph[node]:
                neighbors.append(t[0])
            return neighbors
        except KeyError:
            raise IndexError("That node is not in the graph.")

    def adjacent(self, node_1, node_2):
        """Returns True if node_1 and node_2 share an edge, otherewise False.

        Raises an IndexError if either node does not exist in graph."""
        if self.has_node(node_1) is False:
            raise IndexError("First argument is not in the graph.")
        if self.has_node(node_2) is False:
            raise IndexError("Second argument is not in the graph.")
        edges = self.edges()
        if (node_1, node_2) in edges:
            return True
        else:
            return False

    def depth_first_traversal(self, starting_point):
        """Steps through the graph depth-first.

        Expects a starting point == value of a node in the graph."""
        from dll import DoublyLinkedList
        dll = DoublyLinkedList()
        if self.has_node(starting_point) is False:
            raise IndexError("That starting point is not in the graph.")
        dll.push(starting_point)
        result = []
        while dll.size() > 0:
            working_node = dll.pop()
            if working_node not in result:
                result.append(working_node)
                for node in self.neighbors(working_node):
                    dll.push(node)
        return result

    def breadth_first_traversal(self, starting_point):
        """Steps through the graph breadth-first.

        Expects a starting point == value of a node in the graph."""
        from dll import DoublyLinkedList
        dll = DoublyLinkedList()
        if self.has_node(starting_point) is False:
            raise IndexError("That starting point is not in the graph.")
        dll.push(starting_point)
        result = []
        while dll.size() > 0:
            working_node = dll.shift()
            if working_node not in result:
                result.append(working_node)
                for node in self.neighbors(working_node):
                    dll.push(node)
        return result

    def find_shortest_dijkstra(self, start, end):
        """Shortest distance implementation using our interpretation of
        Dijkstra's algorithm."""
        pass

    def find_shortest_astar(self, start, end):
        """Shortest distance implementation using our interpretation of
        the A* algorithm."""
        pass

if __name__ == '__main__':
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
    print("""
          Graph:  {
                      "node_a": [(node_b, 1), (node_c, 1), (node_d, 1)],
                      "node_b": [(node_e, 1)],
                      "node_c": [],
                      "node_d": [(node_g, 1)],
                      "node_e": [(node_f, 1)],
                      "node_f": [],
                      "node_g": [(node_h, 1)],
                      "node_h": [(node_j, 1), (node_i, 1)],
                      "node_i": [],
                      "node_j": [],
                  }"""
          )
    print('Depth First', instance.depth_first_traversal("a"))
    print('Breadth First', instance.breadth_first_traversal("a"))
