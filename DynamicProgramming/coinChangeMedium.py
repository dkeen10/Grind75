# https://leetcode.com/problems/coin-change/description/
# like leetcode #70 stair climber but harder.


"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0
"""

# Greedy Approach of starting at largest coin and working backwards dowesnt always work.
# Brute Force Approach of finding all combinations works too, but is slow.
# dynamic approach stores the lowest amount of coins needed to make each n amount.
# https://www.youtube.com/watch?v=SIHLJdF4F8A&t=15s


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        O(n*m) time complexity.
        """
        # initialize the dynamic array with 0s and infinities
        dynamic_array = [0] + ([float('inf')] * amount)

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    # if the coin is less than or equal to the amount, then we can use it to make change
                    dynamic_array[i] = min(dynamic_array[i], dynamic_array[i - coin] + 1)
        if dynamic_array[amount] == float('inf'):
            return -1
        return dynamic_array[-1]
    

def main():
    coins = [186,419,83,408]
    amount = 6249
    print(Solution().coinChange(coins, amount))

    coins = [2]
    amount = 3
    print(Solution().coinChange(coins, amount))

    coins = [1]
    amount = 0
    print(Solution().coinChange(coins, amount))


if __name__ == "__main__":
    main()
