class Solution:
  def makePowerNonDescreasing(self, power):
      cnt = 0
      n = len(power)
      for i in range(1, n):
        if power[i] < power[i - 1]:
          cnt += power[i - 1] - power[i]
      return cnt

sl = Solution()
print(sl.makePowerNonDescreasing([3, 4, 1, 6, 2]))
print(sl.makePowerNonDescreasing([3, 2, 1]))