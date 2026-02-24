#Brute Force
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)):
            f = nums[i]

            for j in range(i+1, len(nums)):
                s = nums[j]

                for k in range(j+1, len(nums)):
                    t = nums[k]
                    if f + s + t == 0 and sorted([f,s,t]) not in ans:
                        ans.append(sorted([f,s,t]))
        return ans 

#Time O(n^3 * nlog(n))

