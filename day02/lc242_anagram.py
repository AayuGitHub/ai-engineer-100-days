"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""

class Solution:
    def is_anagram_sort(self, s: str, t: str) -> bool:
        # Quick length check avoid unnecessary sorting
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def is_anagram_countc(self, s:str, t: str) -> bool:
        # Quick length check avoid unnecessary sorting
        if len(s) != len(t):
            return False

        def char_frequency(text: str) -> dict:

            counts = {}

            for char in text:
                counts[char] = counts.get(char, 0) + 1
            return counts

        return char_frequency(s) == char_frequency(t)

solution = Solution()

if __name__ == "__main__":
    print(solution.is_anagram_sort("listen", "silent"))   # True
    print(solution.is_anagram_count("listen", "silent"))  # True
    print(solution.is_anagram_count("rat", "car"))        # False

