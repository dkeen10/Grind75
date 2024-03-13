# https://leetcode.com/problems/product-of-array-except-self/description/


"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Two passes at the original array, iterating forwards with all numbers to the left of target, and backwards with all numbers to the right.

        O(n) time complexity since 2 loops with no nesting.  (so technically O(2n), but that is still linear)
        """
        length = len(nums)
        answer = [0]*length

        # answer[i] contains the product of all the numbers to the left of i
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        # Now for each i in nums, we will calculate the product of all the numbers to the right
        # and multiply it with answer[i]
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer
            

def main():
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))


if __name__ == "__main__":
    main()
