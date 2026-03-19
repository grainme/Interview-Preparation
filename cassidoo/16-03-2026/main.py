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

from typing import List


def fireStationCoverage(plan: List[List[int]]) -> List[List[int]]:
    fireStations = []
    rows = len(plan)
    cols = len(plan[0])

    for i in range(rows):
        for k in range(cols):
            if plan[i][k] == 1:
                fireStations.append((i, k))

    res = plan
    for i in range(rows):
        for k in range(cols):
            curr_cell = (i, k)
            dist = max(cols, rows) + 1

            for fs in fireStations:
                dist = min(dist, abs(curr_cell[0] - fs[0]) + abs(curr_cell[1] - fs[1]))
            res[i][k] = dist

    return res


def main():
    plan = [[2, 0, 1], [0, 2, 0], [1, 0, 2]]
    res = fireStationCoverage(plan)
    print(res)

    plan1 = [[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]]
    res = fireStationCoverage(plan1)
    print(res)


if __name__ == "__main__":
    main()
