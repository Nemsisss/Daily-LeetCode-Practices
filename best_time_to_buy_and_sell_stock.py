class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit= 0
        minPrice= float('inf')

        for i in range(len(prices)):
            if minPrice> prices[i]:
                minPrice=prices[i]
            elif prices[i]-minPrice > maxProfit:
                maxProfit=prices[i]-minPrice

        return maxProfit
