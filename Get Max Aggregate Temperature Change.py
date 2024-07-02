import math
class Solution:
  def getMaxAggregateTemperatureChange(self, tempChange):
    n = len(tempChange)
    prefixSum = [0] * n
    prefix = 0
    for i in range(n):
      prefix += tempChange[i]
      prefixSum[i] = prefix
    
    ans = -math.inf
    for i in range(n):
      # [0: i] + [i:]
      cur = max(prefixSum[i], (prefixSum[-1] - prefixSum[i] + tempChange[i]))
      ans = max(ans, cur)
    return ans

sl = Solution()
print(sl.getMaxAggregateTemperatureChange([6, -2, 5]))