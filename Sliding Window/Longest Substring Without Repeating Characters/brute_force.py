#learn Brute force
#For every index we start a sunstring and extend it until invalid
#It will cover every thing as longest subsring must always start from a index and end in some
#We are choosing every index and checking if this can be in the answer set
#In brute force we give chance to all and assume its the answer until proven otherwise
#Put constrain first, like for null, empty, single, all done in a go

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        ans = 1
        for i in range(len(s)):
            seen = set([s[i]])
            for j in range(i+1, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                ans = max(ans, j - i + 1)
        return ans
    
#Time Complexity: O(n*m)
#Space Complexity: O(m)

#Intuition: We can use a brute-force approach to solve this problem by checking every possible substring of the input string and determining if it contains all unique characters. We can keep track of the longest valid substring found so far.

#Pattern Learned: This brute-force approach is straightforward and easy to understand, but it is not efficient for large input strings. It demonstrates the importance of considering time complexity when designing algorithms, as this approach can lead to a significant number of unnecessary calculations.