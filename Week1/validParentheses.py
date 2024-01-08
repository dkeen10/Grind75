# https://leetcode.com/problems/valid-parentheses/

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Easy intution: the stack is LIFO, so it should be able to handle ordering.
        Time complexity: O(n) since each element gets looked at once.
        """
        n = len(s)
        stack = []

        for character in s:
            if character in "({[":
                stack.append(character)
            else:
                if not stack or 
                

        return False

def main():
    string = "())"
    print(Solution().isValid(string))


if __name__ == "__main__":
    main()
