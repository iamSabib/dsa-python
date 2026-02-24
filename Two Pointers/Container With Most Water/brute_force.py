#Brute Force
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                res = max(res, (j-i) * min(heights[i], heights[j]))
        return res
    
#Time Complexity: O(n^2)
#Space Complexity: O(1)