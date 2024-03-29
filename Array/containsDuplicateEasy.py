# https://leetcode.com/problems/contains-duplicate/description/

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution:
    def containsDuplicate_setApproach_basic(self, nums: list[int]) -> bool:
        """
        Since a set contains only unique elements, this way works.
        """
        nums_set = set(nums)

        if len(nums_set) == len(nums):
            return False
        return True


    def containsDuplicate_setApproach(self, nums: list[int]) -> bool:
        """
        Faster version of above approach since it immediately returns True when duplicate found instead of converting whole array.
        """
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            nums_set.add(nums[i])
        return False

     
    
    def containsDuplicate_sortedApproach(self, nums: list[int]) -> bool:
        sorted_nums = sorted(nums)

        for i in range(len(nums) - 1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
        return False

        
def main():
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))


if __name__ == "__main__":
    main()
