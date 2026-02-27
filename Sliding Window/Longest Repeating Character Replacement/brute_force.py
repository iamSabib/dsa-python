#Brute Force ghetto style
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 1
        for i in range(len(s)):
            seen = defaultdict(int)
            seen[s[i]] += 1
            char_max = s[i]
            for j in range(i + 1, len(s)):
                #check condition
                seen[s[j]] += 1
                #find max
                if seen[s[j]] >= seen[char_max]:
                     char_max = s[j]
                if j - i + 1 > seen[char_max] + k:
                    break
                ans = max(ans, j - i + 1)

        return ans   
                    

#Time Complexity: O(n*m)
#Space Complexity: O(m)

#Intuition: We can use a brute-force approach to solve this problem by checking every possible substring of the input string and determining if it can be transformed into a valid substring by replacing at most k characters. We can keep track of the longest valid substring found so far.
