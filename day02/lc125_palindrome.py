"""

125. Valid Palindrome


It's the same question as your is_palindrome, but solved with a technique called two pointers, without building a cleaned copy of the string. Interviewers like this version because it uses no extra memory.

The idea: put one finger on the first character and one on the last, and move them towards each other.

index:   0    1    2    3
char:    A    b    ,    a
         ↑              ↑
       left           right     'A' vs 'a' → same, ignoring case → move both inward

index:   0    1    2    3
              ↑    ↑
            left right          ',' isn't a letter or digit → move right one step left

              ↑
          left = right          the fingers have met → it's a palindrome ✅

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while(left < right):

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True 



