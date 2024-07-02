import math
class Solution:
  def minimizeSumOfAbsoluteDifferences(self, a, b):
    visited = set()
    n = len(a)
    ans = math.inf
    def dfs(i, total):
      nonlocal ans
      if i >= n:
        ans = min(ans, total)
        return
      for j in range(n):
        if j in visited:
          continue
        total += abs(a[i] - b[j])
        visited.add(j)
        dfs(i + 1, total)
        total -= abs(a[i] - b[j])
        visited.remove(j)

    dfs(0, 0)
    return ans

sl = Solution()
print(sl.minimizeSumOfAbsoluteDifferences([3, 2, 1], [2, 1, 3])) 

