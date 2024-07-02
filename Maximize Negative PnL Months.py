class Solution:
  def maximizeNegativePnLMonths(self, PnL):
    # return 0
    ans = 0
    n = len(PnL)
    def dfs(i, negatives, prefix):
      nonlocal ans
      if i >= n:
        if prefix > 0:
          ans = max(ans, negatives)
        return
      if prefix < 0:
        return
      # (1) not negative
      prefix += PnL[i]
      dfs(i + 1, negatives, prefix)
      prefix -= PnL[i]
      # (2) negative
      prefix -= PnL[i]
      negatives += 1
      dfs(i + 1, negatives, prefix)
      negatives -= 1
      prefix += PnL[i]
    
    dfs(0, 0, 0)
    return ans

sl = Solution()
print(sl.maximizeNegativePnLMonths([5, 3, 1, 2]))
print(sl.maximizeNegativePnLMonths([5, 2, 3, 5, 2, 3]))
print(sl.maximizeNegativePnLMonths([1, 1, 1, 1, 1]))
