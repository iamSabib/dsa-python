#Sliding window ghetto style
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 1
        l = 0
        seen = defaultdict(int)
        ch_max = None
        sc_max = None
        for r, ch in enumerate(s):
            #Adding letter to the window
            seen[ch] += 1

            #Finding-> currently most appeared letter
            if ch != ch_max and seen[ch] > seen[ch_max]: 
                sc_max = ch_max
                ch_max = ch
            elif ch != ch_max and seen[ch] > seen[sc_max]: sc_max = ch


            #check condition
            while r - l + 1 > seen[ch_max] + k:
                #Remove letter from window and update (currently most appeared letter)
                seen[s[l]] -= 1 
                l += 1
                if seen[ch_max] < seen[sc_max]: ch_max, sc_max = sc_max, ch_max
            
            #Valid state, so add to result
            ans = max(ans, r - l + 1)
        
        return ans

#Time Complexity: O(n)
#Space Complexity: O(1)

#Intuition: The sliding window technique allows us to efficiently find the longest substring that can be transformed into a valid substring by replacing at most k characters. We maintain a dynamic window of characters and use a hashmap to keep track of the counts of characters in the current window. When the window size exceeds the allowed limit based on the most frequent character, we shrink the window from the left until the condition is satisfied again.