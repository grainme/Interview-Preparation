"""
Build the Graph
    - Given an edge list, build an adjacency list.
"""

from collections import defaultdict


def build_graph(n: int, edges: list[list[int]], directed: bool = False) -> dict:
    """
    n: number of nodes (0 to n-1)
    edges: [[0,1], [1,2], [2,3], [0,3]]
    Returns: adjacency list as dict
    """
    adj = defaultdict(list)

    for edge in edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        if not directed:
            adj[node2].append(node1)

    return adj


# Example (undirected):
graph = build_graph(4, [[0, 1], [1, 2], [2, 3], [0, 3]])
print(dict(graph))
# → {0: [1,3], 1: [0,2], 2: [1,3], 3: [2,0]}

# Example (directed):
graph = build_graph(4, [[0, 1], [1, 2], [2, 3]], directed=True)
print(dict(graph))
# → {0: [1], 1: [2], 2: [3], 3: []}
