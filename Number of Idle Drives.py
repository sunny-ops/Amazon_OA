from collections import defaultdict
class Solution:
  def numIdleDrives(self, x, y):
    dd_x = defaultdict(list) # map to a list of y - coordinate
    dd_y = defaultdict(list)
    n = len(x)
    for i in range(n):
      curX, curY = x[i], y[i]
      dd_x[curX].append(curY)
      dd_y[curY].append(curX)
    
    cnt = 0
    for key, value in dd_x.items():
      value.sort()
    for key, value in dd_y.items():
      value.sort()
    
    for i in range(n):
      curX, curY = x[i], y[i]
      ys = dd_x[curX] # a list of y coordinates
      xs = dd_y[curY] # a list of x coordinates
      if curY != ys[0] and curY != ys[-1] and curX != xs[0] and curX != xs[-1]:
        cnt += 1
    return cnt


sl = Solution()
print(sl.numIdleDrives([0, 0, 0, 0, 0, 1, 1, 1, 2, -1, -1, -2, -1], [-1, 0, 1, 2, -2, 0, 1, -1, 0, 1, -1, 0, 0]))
print(sl.numIdleDrives([1, 1, 1, 2, 2, 2, 2, 3, 3, 3], [1, 2, 3, 1, 2, 3, 5, 1, 2, 3]))
