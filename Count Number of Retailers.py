import bisect
class Solution:
  def countNumberOfRetailers(self, retailers, requests):
    n = len(retailers)
    sorted_x = sorted([x for x, y in retailers])
    sorted_y = sorted([y for x, y in retailers])
    ans = []
    for x, y in requests:
      ans.append(min(n - bisect.bisect_left(sorted_x, x), n - bisect.bisect_left(sorted_y, y)))
    return ans

sl = Solution()
print(sl.countNumberOfRetailers([[1, 2], [2, 3], [1, 5]], [[1, 1], [1, 4]]))