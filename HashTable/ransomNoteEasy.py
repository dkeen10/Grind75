# https://leetcode.com/problems/ransom-note/description/

"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


class Solution:
    def canConstructBF(self, ransomNote: str, magazine: str) -> bool:
        availableLetters = {}
        for letters in magazine:
            if letters in availableLetters:
                availableLetters[letters] += 1
            else:
                availableLetters[letters] = 1
        for letters in ransomNote:
            if letters in availableLetters and availableLetters[letters] > 0:
                availableLetters[letters] -= 1
            else:
                return False
        return True
            
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)

        # checks that the intersection of the note and magazine objects are equal to the noteCounter object (i.e. that
        # the note counter object is fully contained inside the magazine coutner object)
        # note: cannot use "and", need to use "&" for the bitwise operator
        if noteCounter & magazineCounter == noteCounter:
            return True
        return False       


def main():
    ransomNote = "aa"
    magazine = "aab"
    print(Solution().canConstruct(ransomNote, magazine))

    ransomNote = "a"
    magazine = "b"
    print(Solution().canConstruct(ransomNote, magazine)) 


if __name__ == '__main__':
    main()

