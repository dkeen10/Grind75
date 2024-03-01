# https://leetcode.com/problems/climbing-stairs/description/

"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:   
    def climbStairsMath(self, n: int) -> int:
        solutions = 1

        for i in range(1, n//2 + 1):
            product = 1

            for j in range(i, 2 * i):
                product *= (n - j) / (j - i + 1)

            solutions += product
            
        return solutions
       

    def climbStairsTopDownRecursion(self, n: int) -> int:
        temp_solutions = [-1] * (n + 1)
        return self.solveTopDown(n, temp_solutions)
        

    def solveTopDown(self, n, temp_solutions):
        if n < 0:
            return 0
        if n == 0:
            return 1
        
        # if solution has already been calculated:
        if temp_solutions[n] != -1:
            return temp_solutions[n]
        
        temp_solutions[n] = self.solveTopDown(n - 1, temp_solutions) + self.solveTopDown(n - 2, temp_solutions)

        return temp_solutions[n]


    def climbStairsBottomUpRecursion(self, n: int) -> int:
        temp_solutions = [-1] * (n + 1)
        return self.solveBottomUp(0, n, temp_solutions)
    

    def solveBottomUp(self, i, n, temp_solutions):
        if i == n:
            return 1
        if i > n:
            return 0

        if temp_solutions[i] != -1:
            return temp_solutions[i]

        temp_solutions[i] = self.solveBottomUp(i + 1, n, temp_solutions) + self.solveBottomUp(i + 2, n, temp_solutions)

        return temp_solutions[i]


    def climbStairs_Recursive(self, n: int) -> int:
        if n==1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs_Recursive(n-1) + self.climbStairs_Recursive(n-2)
    

    def climbStairs_dynamic(self, n: int) -> int:
        """
        Question is actually asking to find nth fibonnaci number.

        Bottom up, O(n) time, constant space.
        https://www.youtube.com/watch?v=4ikxUxiEB10&t=0s
        """
        if n == 1:
            return 1
        
        one_before = 1
        two_before = 1
        total = 0

        for i in range(2, n + 1):
            total = one_before + two_before
            two_before = one_before
            one_before = total
        return total


def main():
    n = 3
    print(Solution().climbStairs(n))



if __name__ == "__main__":
    main()

