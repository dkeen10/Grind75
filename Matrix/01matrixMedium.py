# https://leetcode.com/problems/01-matrix/description/


"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 
Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        # get the dimensions of the matrix
        m, n = len(mat), len(mat[0])
        
        # initialize the dp array with a value larger than the maximum possible distance
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        # if the cell contains 0, the distance is 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    # check the distance of the cell to the left and the cell above
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
        
        # check the distance of the cell to the right and the cell below
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < m-1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                if j < n-1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)
        
        return dp
    

    def updateMatrix_2(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < m-1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                if j < n-1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)
        return dp
        


def main():
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    print(Solution().updateMatrix(mat))

    mat = [[0,0,0],[0,1,0],[1,1,1]]
    print(Solution().updateMatrix(mat))


if __name__ == "__main__":
    main()
