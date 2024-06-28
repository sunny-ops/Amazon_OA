class Solution:
  def findMaximumPairs(self, frontend, backend):
    frontend.sort(reverse = True)
    backend.sort()
    i, j = 0, len(backend) - 1
    cnt = 0
    for num in frontend:
      if num > backend[j]:
        j -= 1
        cnt += 1
      else:
        if num > backend[i]:
          cnt += 1
          i += 1
    return cnt

sl = Solution()
print(sl.findMaximumPairs([1, 2, 3], [1, 2, 1]))
print(sl.findMaximumPairs([1, 2, 3, 4, 5], [6, 6, 1, 1, 1]))

      