# https://leetcode.com/problems/rotting-oranges/description/

"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 """

from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        if rows == 0:  
            return -1
        
        cols = len(grid[0])
        
        
        fresh_count = 0
        
        # queue with rotten oranges (for BFS)
        rotten = deque()
        
        # visit each cell in the grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    # add the rotten orange coordinates to the queue
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    # update fresh oranges count
                    fresh_count += 1
        
        # keep track of minutes passed.
        minutes_passed = 0
        
        # If there are rotten oranges in the queue and there are still fresh oranges in the grid keep looping
        while rotten and fresh_count > 0:
            minutes_passed += 1
            
            # process rotten oranges on the current level
            for _ in range(len(rotten)):
                # this is my deque is used instead of list, since popleft() doesnt realloc memory
                x, y = rotten.popleft()
                
                # visit all the adjacent cells
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    # calculate the coordinates of the adjacent cell
                    xx, yy = x + dx, y + dy
                    # ignore the cell if it is out of the grid boundary
                    if xx < 0 or xx == rows or yy < 0 or yy == cols:
                        continue
                    # ignore the cell if it is empty '0' or visited before '2'
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                        
                    # update the fresh oranges count
                    fresh_count -= 1
                    
                    # mark the current fresh orange as rotten
                    grid[xx][yy] = 2
                    
                    # add the current rotten to the queue
                    rotten.append((xx, yy))

        # return -1 if there are fresh oranges left in the grid (there were no adjacent rotten oranges to make them rotten)
        return minutes_passed if fresh_count == 0 else -1
    

def main():
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(Solution().orangesRotting(grid))

    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(Solution().orangesRotting(grid))

    grid = [[0,2]]
    print(Solution().orangesRotting(grid))


if __name__ == '__main__':
    main()       
        