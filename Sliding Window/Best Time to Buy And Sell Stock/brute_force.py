#Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > profit: profit = prices[j] - prices[i]
        return profit
        
#Time Complexity: O(n^2)
#Space Complexity: O(1)

#Intuion: We can use two nested loops to check every possible pair of buy and sell days, calculating the profit for each pair and keeping track of the maximum profit found.

#Pattern Learned: This brute force approach is straightforward but inefficient for large input sizes. It serves as a baseline solution before optimizing with more efficient algorithms like the sliding window technique.