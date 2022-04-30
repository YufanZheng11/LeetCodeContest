"""
https://leetcode.com/contest/biweekly-contest-77/problems/escape-the-spreading-fire/

You are given a 0-indexed 2D integer array grid of size m x n which represents a field. Each cell has one of three values:

0 represents grass,
1 represents fire,
2 represents a wall that you and fire cannot pass through.
You are situated in the top-left cell, (0, 0), and you want to travel to the safehouse at the bottom-right cell, (m - 1, n - 1). Every minute, you may move to an adjacent grass cell. After your move, every fire cell will spread to all adjacent cells that are not walls.

Return the maximum number of minutes that you can stay in your initial position before moving while still safely reaching the safehouse. If this is impossible, return -1. If you can always reach the safehouse regardless of the minutes stayed, return 109.

Note that even if the fire spreads to the safehouse immediately after you have reached it, it will be counted as safely reaching the safehouse.

A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).



Example 1:


Input: grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
Output: 3
Explanation: The figure above shows the scenario where you stay in the initial position for 3 minutes.
You will still be able to safely reach the safehouse.
Staying for more than 3 minutes will not allow you to safely reach the safehouse.
Example 2:


Input: grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
Output: -1
Explanation: The figure above shows the scenario where you immediately move towards the safehouse.
Fire will spread to any cell you move towards and it is impossible to safely reach the safehouse.
Thus, -1 is returned.
Example 3:


Input: grid = [[0,0,0],[2,2,0],[1,2,0]]
Output: 1000000000
Explanation: The figure above shows the initial grid.
Notice that the fire is contained by walls and you will always be able to safely reach the safehouse.
Thus, 109 is returned.


Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 300
4 <= m * n <= 2 * 104
grid[i][j] is either 0, 1, or 2.
grid[0][0] == grid[m - 1][n - 1] == 0
"""

from copy import deepcopy


class Solution:
    def maximumMinutes(self, grid):
        gridPerMinute = self.getGridPerMinutes(grid)
        maxMinute = -1

        for minute in gridPerMinute:
            if self.canEscape(minute, gridPerMinute):
                if len(gridPerMinute) == 1:
                    return 1000000000
                maxMinute = max(maxMinute, minute)
        return maxMinute

    def getGridPerMinutes(self, grid):
        grid = deepcopy(grid)
        m, n = len(grid), len(grid[0])

        gridPerMinute = {}

        minute = 0
        gridPerMinute[minute] = grid

        while True:
            oldGrid = gridPerMinute[minute]
            newGrid = deepcopy(oldGrid)
            for i in range(m):
                for j in range(n):
                    if oldGrid[i][j] == 1:
                        for u, v in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                            if 0 <= u < m and 0 <= v < n and oldGrid[u][v] == 0:
                                newGrid[u][v] = 1
            if self.sameGrid(gridPerMinute[minute], newGrid):
                break
            minute += 1
            gridPerMinute[minute] = newGrid

        return gridPerMinute

    def sameGrid(self, grid1, grid2):
        m, n = len(grid1), len(grid1[0])
        for i in range(m):
            for j in range(n):
                if grid1[i][j] != grid2[i][j]:
                    return False
        return True

    def canEscape(self, minute, gridPerMinute):
        grid = gridPerMinute[minute]
        m, n = len(grid), len(grid[0])
        queue = [[(0, 0), [(0, 0)], minute]]
        while queue:
            node, path, minute = queue.pop(0)
            i, j = node
            if i == m - 1 and j == n - 1:
                return True
            if len(gridPerMinute) != 1:
                if minute == max(gridPerMinute.keys()):
                    continue
                nextGrid = gridPerMinute[minute + 1]
            else:
                nextGrid = grid
            for u, v in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= u < m and 0 <= v < n and (u, v) not in path:
                    if nextGrid[u][v] == 0:
                        queue.append([(u, v), path + [(u, v)], minute + 1])
                    elif u == m-1 and v == n-1 and gridPerMinute[minute][u][v] == 0:
                        queue.append([(u, v), path + [(u, v)], minute + 1])
        return False