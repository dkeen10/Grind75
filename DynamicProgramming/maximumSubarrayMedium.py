# https://leetcode.com/problems/maximum-subarray/description/

"""
Given an integer array nums, find the
subarray
with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # highest sum found so far
        max_sum = nums[0]

        # current sum of subarray
        current_sum = nums[0]
            
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
            

def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))

    nums = [5,4,-1,7,8]
    print(Solution().maxSubArray(nums))
    

if __name__ == "__main__":
    main()
