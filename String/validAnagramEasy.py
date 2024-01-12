# https://leetcode.com/problems/valid-anagram/description/

"""
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution:
    def isAnagramBruteForce(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True


    def isAnagramHashing(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_map = [0] * 26

        for i in range((len(s))):
            char_map[ord(s[i]) - ord('a')] += 1
            char_map[ord(t[i]) - ord('a')] -= 1

        return all(count == 0 for count in char_map)
    

def main():
    s = "rat"
    t = "tar"
    print(Solution().isAnagramHashing(s, t))


if __name__ == "__main__":
    main()
