#two pointers

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            #profit calc
            if prices[r] - prices[l] > profit:
                profit = prices[r] - prices[l]
            else:
                if prices[r] < prices[l]:
                    l = r
            r += 1
        return profit
    
#Time Complexity: O(n)
#Space Complexity: O(1)

#Intuion: We can use two pointers to keep track of the minimum price (buying day) and the maximum profit (selling day). We iterate through the list of prices, updating the minimum price and calculating the profit at each step, while keeping track of the maximum profit found.

#Pattern Learned: This two-pointer approach is efficient and allows us to solve the problem in linear time. It demonstrates how we can optimize a brute-force solution by using pointers to track relevant information and avoid unnecessary calculations.