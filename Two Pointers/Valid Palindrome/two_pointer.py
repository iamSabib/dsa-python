#two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
       l, r = 0, len(s)-1
       s = s.lower()
       
       while l < r:
            while l < r and not self.alpNum(s[l]):
                l += 1
            while l < r and not self.alpNum(s[r]):
                r -= 1
            if s[l] != s[r]: return False
            l, r = l + 1, r - 1

       return True

    def alpNum(self, c):
        return (ord('a') <= ord(str(c)) <= ord('z') or
                ord('A') <= ord(str(c)) <= ord('Z') or
                ord('0') <= ord(str(c)) <= ord('9') )

        