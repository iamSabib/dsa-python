#Dynamic Programing

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0

        for i in prices:
            if i < lowest: lowest = i
            max_profit = max(max_profit, i - lowest)
            
        return max_profit
        
#Time Complexity: O(n)
#Space Complexity: O(1)

#Intuion: We can iterate through the list of prices while keeping track of the lowest price seen so far and the maximum profit that can be achieved by selling at the current price. This way, we can calculate the maximum profit in a single pass through the list.

#Pattern Learned: This dynamic programming approach is efficient and allows us to solve the problem in linear time. It demonstrates how we can optimize a brute-force solution by keeping track of relevant information (lowest price and maximum profit) as we iterate through the list, avoiding unnecessary calculations.