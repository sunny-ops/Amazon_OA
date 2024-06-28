class Solution:
  def maximizeSubtreeProduct(self, n: int, edges) -> int:
      memo = dict()
      def dp(i):
          if i == 1:
              return 1
          if i <= 0:
              return 0
          if i in memo:
              return memo[i]
          ans = i
          for j in range(1, i):
            # print("i, j", i, j)
            # print(j, i - j)
            ans = max(ans, dp(j) * dp(i - j))
          memo[i] = ans
          return ans

      return dp(n)

sl = Solution()
print(sl.maximizeSubtreeProduct(5, [[1, 2], [2, 3], [3, 4], [4, 5]]))
