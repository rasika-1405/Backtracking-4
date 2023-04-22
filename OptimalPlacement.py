"""
Rasika Sasturkar
Time Complexity: O(hw * hwCn), h is height, w is width, n is no. of buildings
Space Complexity: O(hw)
"""

import collections
import math


def findMinDistance(height, width, n):
    h = height
    w = width
    min_dist = math.inf

    grid = [[-1 for _ in range(w)] for _ in range(h)]

    def bfs(grid):
        nonlocal min_dist
        queue = collections.deque()
        visited = [[False for _ in range(w)] for _ in range(h)]
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0:
                    queue.append([i, j])
                    visited[i][j] = True

        # process bfs
        dist = 0
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                for dirn in dirs:
                    nr = curr[0] + dirn[0]
                    nc = curr[1] + dirn[1]
                    if nr >= 0 and nc >= 0 and nr < h and nc < w and not visited[nr][nc]:
                        queue.append([nr, nc])
                        visited[nr][nc] = True

            dist += 1
        min_dist = min(min_dist, dist - 1)

    def backtrack(grid, n, idx):
        # base case
        if n == 0:
            bfs(grid)

        # logic
        for j in range(idx, h * w):
            r = j // w
            c = j % w
            grid[r][c] = 0  # action
            backtrack(grid, n - 1, j + 1)  # recurse
            grid[r][c] = -1  # backtrack

    backtrack(grid, n, 0)
    return min_dist


def main():
    """
    Main function - example problem to show the working.
    """
    print(findMinDistance(4, 4, 3))  # returns 2


if __name__ == "__main__":
    main()
