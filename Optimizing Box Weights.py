class Solution:
  def minimalHeaviestSetA(self, arr):
      arr.sort(reverse = True)
      A = 0
      B = sum(arr)
      ans = []
      i = 0
      while i < len(arr) and A < B:
        ans.append(arr[i])
        A += arr[i]
        B -= arr[i]
        i += 1
      return ans

sl = Solution()
print(sl.minimalHeaviestSetA([5, 3, 2, 4, 1, 2]))