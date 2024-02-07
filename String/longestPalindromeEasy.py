# https://leetcode.com/problems/longest-palindrome/description/


"""Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        make a set to hold leftover, non-matching characters
        loop through the characters in the string.  if they aren't in the set yet, add to set, else remove from set (paired for palindrome)
        longest palindrome is length of string minus length of characters still in the set of leftover characters.
        """
        chars = set()
        for char in s:
            if char in chars:
                chars.remove(char)
            else:
                chars.add(char)
        return len(s) - len(chars) + 1 if chars else len(s)


def main():
    s = "abccccdd"
    print(Solution().longestPalindrome(s))


if __name__ == "__main__":
    main()

