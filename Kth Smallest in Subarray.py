# from sortedcontainers import SortedList
import heapq
class Solution:
  def kthSmallestInSubarray(self, arr, k: int, m: int):
    # sl = SortedList(arr[:m])
    # n = len(arr)
    # ans = [sl[k - 1]]
    # for i in range(m, n):
    #   sl.remove(arr[i - m])
    #   sl.add(arr[i])
    #   ans.append(sl[k - 1])
    n = len(arr)
    ans = []
    for i in range(n - m + 1):
      h = arr[i: i + m]
      heapq.heapify(h)
      for _ in range(k - 1):
        heapq.heappop(h)
      ans.append(h[0])
      
    return ans

sl = Solution()
print(sl.kthSmallestInSubarray([3, 1, 4, 2], 2, 3))