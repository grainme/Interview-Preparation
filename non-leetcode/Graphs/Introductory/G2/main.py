"""
BFS — Find All Nodes at Distance K

Given a graph and a start node, return all nodes exactly k edges away.
"""

from collections import defaultdict, deque


def build_graph(n: int, edges: list[list[int]], directed: bool = False) -> dict:
    adj = defaultdict(list)

    for edge in edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        if not directed:
            adj[node2].append(node1)

    return adj


def nodes_at_distance(n: int, edges: list[list[int]], start: int, k: int) -> list[int]:
    adj = build_graph(n, edges)
    visited = set()
    q = deque()

    q.append(start)
    visited.add(start)
    while q:
        sz = len(q)
        for i in range(sz):
            node = q.popleft()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        k -= 1
        if k == 0:
            break
    return list(q)


# Example:
res = nodes_at_distance(5, [[0, 1], [1, 2], [1, 3], [3, 4]], 0, 2)
print(res)
# [2, 3]

res = nodes_at_distance(5, [[0, 1], [1, 2], [1, 3], [3, 4]], 0, 3)
print(res)
# [4]

res = nodes_at_distance(3, [[0, 1], [1, 2], [0, 2]], 0, 1)
print(res)
# [1, 2]
