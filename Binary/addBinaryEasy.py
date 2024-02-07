# https://leetcode.com/problems/add-binary/description/

"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

 """


class Solution:
    def addBinary_cheat(self, a: str, b: str) -> str:
       return bin(int(a, 2) + int(b, 2))


def main():
    a = "11"
    b = "1"
    print(Solution().addBinary_cheat(a, b))

    # a = "1010"
    # b = "1011"
    # print(Solution().addBinary(a, b))



if __name__ == "__main__":
    main()

