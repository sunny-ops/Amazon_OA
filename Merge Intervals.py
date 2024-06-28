class Solution:
  def merge(self, intervals):
    ans = []
    intervals.sort()
    start, end = intervals[0]
    for i in range(1, len(intervals)):
      curS, curE = intervals[i]
      if curS <= end:
        end = max(end, curE)
      else:
        ans.append([start, end])
        start, end = curS, curE
    
    ans.append([start, end])
    return ans

sl = Solution()
print(sl.merge([[1,3],[2,6],[8,10],[15,18]]))
      