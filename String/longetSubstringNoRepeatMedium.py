# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

"""
Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 """


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        slow_pointer= 0
        used_characters = set()


        for i in range(len(s)):
            if s[i] not in used_characters:
                used_characters.add(s[i])
                longest_substring = max(longest_substring, i - slow_pointer + 1)
            else:
                while s[i] in used_characters:
                    used_characters.remove(s[slow_pointer])
                    slow_pointer += 1
                used_characters.add(s[i])
        return longest_substring


def main():
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))

    s = "bbbbb"
    print(Solution().lengthOfLongestSubstring(s))

    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))



if __name__ == "__main__":
    main()

