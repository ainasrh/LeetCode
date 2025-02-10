class Solution(object):
    def buyChoco(self, prices, money):
        prices.sort()

        balance = money-(prices[0]+prices[1])
        return money if money<(prices[0]+prices[1]) else balance
        #     print(money)
        # else:
        #     print(balance)
        
    