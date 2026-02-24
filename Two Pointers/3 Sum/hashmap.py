# hashmap
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # seen = set(nums)
        seen = defaultdict(int)
        for v in nums:
            seen[v] += 1

        ans = {}
        for i in range(len(nums)):
            f = nums[i]
            seen[f] -= 1
            #2 sum
            for j in range(i+1, len(nums)):
                s = nums[j]
                seen[s] -= 1
                t = -(f + s)
                if t in seen and seen[t]:
                    #order sort
                    big = max(f, s, -f-s)
                    small = min(f, s, -f-s)
                    rem = -(big + small)
                    ans[(big, small, rem)] = 1

                seen[s] += 1
            seen[f] += 1
        
        return [list(x) for x in ans.keys()]

#Time O(n^2)
#Space O(n)
