import math
class Solution:
  def maximumStability(self, reliability, availability) -> int:
      n = len(reliability)
      arr = [(reliability[i], availability[i]) for i in range(n)]
      arr.sort(key = lambda x: x[1], reverse = True)
      print(arr)
      prefix = 0
      minimum = math.inf
      ans = 0
      for i in range(n):
        prefix += arr[i][0]
        minimum = min(minimum, arr[i][1])
        ans = max(ans, prefix * minimum)
      return ans

sl = Solution()
print(sl.maximumStability([1, 2, 2], [1, 1, 3]))