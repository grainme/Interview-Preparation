"""
You're given a 2D grid representing a city where each cell is either empty (0),
a fire station (1), or a building (2).

Fire stations can serve buildings based on horizontal + vertical moves only.

Return a 2D grid where each cell shows the minimum distance to the nearest
fire station.

Examples:

> fireStationCoverage([
  [2, 0, 1],
  [0, 2, 0],
  [1, 0, 2]
])
> [[2, 1, 0],
   [1, 2, 1],
   [0, 1, 2]]

> fireStationCoverage([
  [1, 0, 0, 1],
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 0, 0, 1]
])
> [[0, 1, 1, 0],
   [1, 2, 2, 1],
   [1, 2, 2, 1],
   [0, 1, 1, 0]]
"""

from collections import deque
from typing import List


def fireStationCoverage(plan: List[List[int]]) -> List[List[int]]:
    rows = len(plan)
    cols = len(plan[0])
    queue = deque()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dist = [[max(rows, cols) + 1] * cols for _ in range(rows)]

    for i in range(rows):
        for k in range(cols):
            if plan[i][k] == 1:
                dist[i][k] = 0
                queue.append((i, k))

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] > dist[r][c] + 1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))

    return dist


def main():
    plan = [[2, 0, 1], [0, 2, 0], [1, 0, 2]]
    res = fireStationCoverage(plan)
    print(res)

    plan1 = [[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]]
    res = fireStationCoverage(plan1)
    print(res)


if __name__ == "__main__":
    main()
