# https://leetcode.com/problems/valid-parentheses/

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValidBruteForce(self, s: str) -> bool:
        stack = []
        n = len(s)

        for character in s:
            # add open parenthesis
            if character in "({[":
                stack.append(character)
            
            else:
                # check for invalids
                if n == 0 or (character == ")" and stack[-1] != "(") or (character == ")" and stack[-1] != "(") or (character == ")" and stack[-1] != "("):
                    return False;
        
                # remove closed parenthesis
                stack.pop()
        
        # after looping, a valid string should be empty.
        return len(stack) == 0


    def isValid(self, s: str) -> bool:
        """
        Easy intution: the stack is LIFO, so it should be able to handle ordering.
        Time complexity: O(n) since each element gets looked at once.
        """
        n = len(s)

        # a list acts as a stack if you only operate from the end, so using only append() and pop()
        stack = []

        pairs = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for character in s:
            # check if character in keys of dictionary, so "({["
            if character in pairs:
                stack.append(character)
            
            # checks if stack is empty, or if character ")}]" matches its corresponding type, in which case it removes both.
            elif n == 0 or character != pairs[stack.pop()]:
                return False
        
        # after going through and removing matching, an empty string will return True and a non empty string will return False.
        return len(stack) == 0;
    
                
            

def main():
    string = "([])"
    print(Solution().isValidBruteForce(string))
    print(Solution().isValid(string))


if __name__ == "__main__":
    main()
