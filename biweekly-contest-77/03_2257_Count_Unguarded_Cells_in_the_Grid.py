"""
https://leetcode.com/contest/biweekly-contest-77/problems/count-unguarded-cells-in-the-grid/

ou are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.


Example 1:

Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.

Example 2:

Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.


Constraints:

1 <= m, n <= 105
2 <= m * n <= 105
1 <= guards.length, walls.length <= 5 * 104
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
All the positions in guards and walls are unique.
"""


class Solution:
    def countUnguarded(self, m: int, n: int, guards, walls) -> int:
        board = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in guards:
            board[i][j] = 1
        for i, j in walls:
            board[i][j] = 2

        for i, j in guards:
            # Left
            for u in range(i - 1, -1, -1):
                brk = self.fillCell(board, u, j)
                if brk:
                    break
            # Right
            for u in range(i + 1, m):
                brk = self.fillCell(board, u, j)
                if brk:
                    break
            # Up
            for v in range(j - 1, -1, -1):
                brk = self.fillCell(board, i, v)
                if brk:
                    break
            # Down
            for v in range(j + 1, n):
                brk = self.fillCell(board, i, v)
                if brk:
                    break

        nCells = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    nCells += 1
        return nCells

    def fillCell(self, board, i, j):
        val = board[i][j]
        brk = False
        if val == 0:
            board[i][j] = 3
        elif val == 1:
            brk = True
        elif val == 2:
            brk = True
        elif val == 3:
            pass
        return brk

