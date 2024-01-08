# https://leetcode.com/problems/two-sum/

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


class Solution:
    def twoSumBruteForce(self, nums: list[int], target: int) -> list[int]:
        """O(n^2) Time complexity since we loop through the array twice."""
        n = len(nums)
        for i in range(n - 1):
            for j in range (i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    

    def twoSumHashTableTwoPass(self, nums: list[int], target: int) -> list[int]:
        """O(n) time complexity since we take two passes through the array so it still scales linearly."""
        numMap = {}
        n = len(nums)
        
        #build hash table:
        for i in range(n):
            numMap[nums[i]] = i
            print(numMap)

        #find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return[]


    def twoSumHashTableOnePass(self, nums: list[int], target: int) -> list[int]:
        """O(n) time complexity since we take just one pass through the array"""

        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSumBruteForce(nums, target))
    print(Solution().twoSumHashTableTwoPass(nums, target))
    print(Solution().twoSumHashTableOnePass(nums, target))


if __name__ == "__main__":
    main()
