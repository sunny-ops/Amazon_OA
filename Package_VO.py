from collections import deque
from collections import Counter
class Solution:


# W = 100, H = 200, L = 1000

# w 50, h 50, l 100 -> w 100, h 50, l 50
# w 50, h 50, l 200 -> w 50, h 200, l 50
# w 50, h 50, l 300 -> w 50, h 50, l 300

    
    def isValid(self, a, b, W, H):
        return a <= W and b <= H
    
    def numberOfPackages(self, W, H, L, arr):
        cnt = 0
        total = 0
        for w, h, l in arr:
            a, b, c = sorted([w, h, l])
            if self.isValid(b, c, W, H):
                l = a
            elif self.isValid(a, c, W, H):
                l = b
            elif self.isValid(a, b, W, H):
                l = c
            else:
                continue
            if total + l <= L:
                total += l
                cnt += 1
        
        print("total", total)
        return cnt



sl = Solution()
print(sl.numberOfPackages(100, 200, 1000, [[50, 50, 100], [50, 50, 200], [50, 50, 300]]))