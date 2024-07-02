class Solution:
  def maxNumberOfBalancedShipments0(self, weight):
      memo = dict()
      def dp(j):
          if j <= 0:
              return 0
          ans = 0
          prefix_max = weight[j]
          for i in range(j - 1, -1, -1):
              prefix_max = max(prefix_max, weight[i])
              if prefix_max > weight[j]:
                  ans = max(ans, 1 + dp(i - 1))
          memo[j] = ans
          return ans
      res =  dp(len(weight) - 1)
      return res
          
  def maxNumberOfBalancedShipments(self, weight):
        n = len(weight)
        f = [0] * n
        for i in range(n):
            prefix_max = weight[i]
            j = i - 1
            while j >= 0:
                prefix_max = max(prefix_max, weight[j])
                if prefix_max > weight[i]:
                    f[i] = max(f[i], 1 + (f[j - 1] if j - 1 >= 0 else 0))
                j -= 1
        return f[-1]
  
  def maxNumberOfBalancedShipments1(self, weight): 
      n = len(weight)
      f = [None for i in range(n + 1)]
      g = [None for i in range(n + 1)]
      h = [None for i in range(n)]

      st = []
      stsize = 0
      for i in range(n - 1, -1, -1):
          while stsize > 0 and weight[st[-1]] < weight[i]:
              h[st[-1]] = i
              stsize -= 1
              st.pop()
          st.append(i)
          stsize += 1

      f[0] = 0
      g[0] = 0
      for i in range(1, n + 1):
          f[i] = 0
          if h[i - 1] != None:
              f[i] = 1 + g[h[i - 1]]
          g[i] = max(g[i - 1], f[i])

      return f[n]



sl = Solution()

print(sl.maxNumberOfBalancedShipments0([9, 8, 5, 4, 7, 2, 16, 5, 2, 7]))
print(sl.maxNumberOfBalancedShipments([9, 8, 5, 4, 7, 2, 16, 5, 2, 7]))
print(sl.maxNumberOfBalancedShipments1([9, 8, 5, 4, 7, 2, 16, 5, 2, 7]))