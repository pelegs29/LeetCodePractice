# 1672. Richest Customer Wealth

def maximumWealth(self, accounts: list[list[int]]) -> int:
    for i in range(0, len(accounts)):
        accounts[i] = [sum(accounts[i])]
    return max(accounts)[0]


