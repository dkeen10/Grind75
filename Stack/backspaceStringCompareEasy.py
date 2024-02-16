# https://leetcode.com/problems/backspace-string-compare/description/


"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

 """


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for character in s:
            if character == "#":
                if len(s_stack) > 0:
                    s_stack.pop()
            else:
                s_stack.append(character)
        
        for character in t:
            if character == "#":
                if len(t_stack) > 0:
                    t_stack.pop()
            else:
                t_stack.append(character)

        return s_stack == t_stack


def main():
    s = "ab#c"
    t = "ad#c"
    print(Solution().backspaceCompare(s, t))

    s = "ab##"
    t = "c#d#"
    print(Solution().backspaceCompare(s, t))

    s = "a#c"
    t = "b"
    print(Solution().backspaceCompare(s, t))


if __name__ == "__main__":
    main()
