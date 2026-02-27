# Sliding window
# condition: No repearing character -> using hashmap

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l, r = 0, 0
        l = 0
        seen = {}
        res = 0
        for r in range(len(s)):
            #check condition

            while seen.get(s[r]):
                seen[s[l]] -= 1
                l += 1
            
            seen[s[r]] = 1
            res = max(res, r-l+1)

        return res

#Time O(n)
#Spcae O(1)
        
#Intuition: The sliding window technique allows us to efficiently find the longest substring without repeating characters by maintaining a dynamic window of characters. We use a hashmap to keep track of the characters in the current window and their counts. When we encounter a repeating character, we shrink the window from the left until the condition is satisfied again.

#Pattern Learned: The sliding window approach is a powerful technique for solving problems that involve contiguous sequences, such as substrings or subarrays. It helps to optimize the time complexity by avoiding unnecessary recalculations and allows us to maintain a dynamic range of elements while iterating through the input.