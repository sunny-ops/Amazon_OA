import math
class Solution:
  def findEarliestMonth(self, stockPrice):
    prefix = 0
    total = sum(stockPrice)
    n = len(stockPrice)
    minimumPC = math.inf
    for i in range(len(stockPrice) - 1):
      prefix += stockPrice[i]
      total -= stockPrice[i]
      netPriceChange = abs(total // (n - i - 1) - prefix // (i + 1))
      
      if netPriceChange < minimumPC:
        ans = i + 1
        minimumPC = netPriceChange
    
    return ans
  
sl = Solution()
print(sl.findEarliestMonth([1, 3, 2, 3]))
print(sl.findEarliestMonth([1, 3, 2, 4, 5]))