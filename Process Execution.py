import bisect
class Solution:
  def processExecution(self, power, minPower, maxPower):
      power.sort()
      n = len(power)
      ans = []
      prefix = 0
      prefixArr = [0] * n
      for i in range(n):
         prefix += power[i]
         prefixArr[i] = prefix

      for i in range(len(minPower)):
         minIdx = bisect.bisect_left(power, minPower[i])
         maxIdx = bisect.bisect_right(power, maxPower[i])
         print(minIdx, maxIdx)
         if maxIdx == minIdx:
            ans.append([0, 0])
         else:
            ans.append([maxIdx - minIdx, prefixArr[maxIdx - 1] - prefixArr[minIdx] + power[minIdx]])
      return ans

sl = Solution()
# print(sl.processExecution([7, 6, 8, 10], [6, 3, 4], [10, 7, 9]))
print(sl.processExecution([11, 11, 11], [8, 13], [11, 100]))
      
  
  