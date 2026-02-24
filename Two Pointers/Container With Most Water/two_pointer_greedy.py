#two pointers, greedy
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while r > l:
            h = min(heights[l], heights[r])
            area = (r - l) * h
            res = max(res, area)

            if heights[l] > heights[r]:
                r -= 1
            else: l += 1
        
        return res

#Time O(n)
#Space O(1)
