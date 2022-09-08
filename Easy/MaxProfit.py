# 121. Best Time to Buy and Sell Stock


def maxProfit(self, prices: list[int]) -> int:
    max_profit = 0
    buy = 0
    sell = 1
    while sell < len(prices):
        curr_profit = prices[sell] - prices[buy]
        if prices[buy] < prices[sell]:
            max_profit = max(curr_profit, max_profit)
        else:
            buy = sell
        sell += 1
    return max_profit
