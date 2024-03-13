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


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        minTime = 0
        freshOranges = 0
        rottenOranges = []

        # count the number of fresh oranges and store the rotten oranges in a list
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    rottenOranges.append((i, j))

        # if there are no fresh oranges, return 0
        if freshOranges == 0:
            return 0
        
        # if there are no rotten oranges, return -1
        if not rottenOranges:
            return -1
        
        # while there are fresh oranges and there are rotten oranges
        while freshOranges > 0 and rottenOranges:
            newRottenOranges = []
            for i, j in rottenOranges:
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[i]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        freshOranges -= 1
                        newRottenOranges.append((x, y))
            rottenOranges = newRottenOranges
            minTime += 1

        return minTime if freshOranges > 0 else -1
    

def main():
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(Solution().orangesRotting(grid))

    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(Solution().orangesRotting(grid))

    grid = [[0,2]]
    print(Solution().orangesRotting(grid))


if __name__ == '__main__':
    main()       
        