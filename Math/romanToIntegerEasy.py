# https://leetcode.com/problems/roman-to-integer/description/


"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
"""


class Solution:
    def romanToInt_Naive(self, s: str) -> int:
        if len(s) == 1:
            if s[0] == "I":
                return 1
            if s[0] == "V":
                return 5
            if s[0] == "X":
                return 10
            if s[0] == "L":
                return 50
            if s[0] == "C":
                return 100
            if s[0] == "D":
                return 500
            if s[0] == "M":
                return 1000
        
        numerals = list(s)
        print(numerals)
        base_10_num = 0

        for i in range(len(s) - 1, 0, -1):
            if numerals[i] == "I":
                base_10_num += 1
            elif numerals[i] == "V":
                if numerals[i - 1] == "I":
                    base_10_num -= 1
                    i -= 2
                base_10_num += 5
            elif numerals[i] == "X":
                if numerals[i - 1] == "I":
                    base_10_num -= 1
                    i -= 2
                base_10_num += 10
            elif numerals[i] == "L":
                if numerals[i - 1] == "X":
                    base_10_num -= 10
                    i -= 2
                base_10_num += 50
            elif numerals[i] == "C":
                if numerals[i - 1] == "X":
                    base_10_num -= 10
                    i -= 2
                base_10_num += 100
            elif numerals[i] == "D":
                if numerals[i - 1] == "C":
                    base_10_num -= 100
                    i -= 2
                base_10_num += 500
            elif numerals[i] == "M":
                if numerals[i - 1] == "C":
                    base_10_num -= 100
                    i -= 2
                base_10_num += 1000

        if numerals[0] == "I" and (numerals[1] != "V" and numerals[1] != "X"):
            base_10_num += 1
        elif numerals[0] == "X" and (numerals[1] == "L" and numerals[1] == "C"):
             base_10_num += 10
        elif numerals[0] == "C" and (numerals[1] == "D" and numerals[1] == "M"):
            base_10_num += 100
        elif numerals[0] == "V":
            base_10_num += 5
        elif numerals[0] == "L":
            base_10_num += 50
        elif numerals[0] == "D":
            base_10_num += 500
        elif numerals[0] == "M":
            base_10_num += 1000
        return base_10_num
    

    def romanToInt_Hashtable(self, s: str) -> int:
        numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        base_10_num = 0
        
        # we ignore the last element and add it at the end, since it can't be a subtraction.
        for i in range(len(s) - 1):
            # since the numerals are ordered from largest to smallest, if smaller one is to the left of a larger, it is a subtraction.
            if numerals[s[i]] < numerals[s[i+1]]:
                base_10_num -= numerals[s[i]]
            else:
                base_10_num += numerals[s[i]]
            
        return base_10_num + numerals[s[-1]]
            

def main():
    s = "III"
    print(Solution().romanToInt_Hashtable(s))

    s = "IV"
    print(Solution().romanToInt_Hashtable(s))

    s = "MCMXCIV"
    print(Solution().romanToInt_Hashtable(s))


if __name__ == "__main__":
    main()
