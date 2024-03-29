# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""


class Solution:
    def maxProfitBruteForce(self, prices: list[int]) -> int:
        """
        O(n^2) time complexity since looping through list twice.
        """
        maxProfit = 0
        n = len(prices)
        for i in range(n -1):
            for j in range(i + 1, n):
                if prices[j] - prices[i] > maxProfit:
                    maxProfit = prices [j] - prices[i]
        return maxProfit


    def maxProfit(self, prices: list[int]) -> int:
        """
        O(n) time complexity since only loops once."""
        maxProfit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                if sell - buy > maxProfit:
                    maxProfit = sell - buy
            else:
                buy = sell
        return maxProfit


def main():
    inputPrices = [7,1,5,3,6,4]
    print(Solution().maxProfit(inputPrices))
   

if __name__ == "__main__":
    main()
