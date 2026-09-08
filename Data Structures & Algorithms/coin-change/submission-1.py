class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0

            if amount < 0:
                return -1

            if amount in memo:
                return memo[amount]

            res = -1

            for coin in coins:
                num = dfs(amount - coin)

                if num != -1:
                    if res == -1 or num + 1 < res:
                        res = num + 1

            memo[amount] = res
            return res

        return dfs(amount)