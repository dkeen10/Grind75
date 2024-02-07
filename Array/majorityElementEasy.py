# https://leetcode.com/problems/majority-element/description/

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement_midpoint(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
    
    def majorityElement_simple(self, nums: list[int]) -> int:
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        return max(nums_dict, key=nums_dict.get)
    

def main():
    nums = [3, 2, 3]
    print(Solution().majorityElement_simple(nums))

    # nums = [2, 2, 1, 1, 1, 2, 2]
    # solution = Solution()
    # print(solution.majorityElement(nums))


if __name__ == "__main__":
    main()

