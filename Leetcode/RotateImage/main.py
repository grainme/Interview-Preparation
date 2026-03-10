# https://leetcode.com/problems/rotate-image/description/
from typing import List


class Solution:
    def rotate(self, mat: List[List[int]]):
        n = len(mat)
        mat.reverse()
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            self.rotate(mat)
            if mat == target:
                return True
        return False
