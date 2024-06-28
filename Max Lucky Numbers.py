class Solution:
  def getMaxLuckyNumber(self, x: int, y: int, n: int):
    # ans = 0
    
    # i = 0
    # while i * x <= n:
    #   remain = n - i * x
    #   if remain % y != 0:
    #     i += 1
    #     continue
    #   else:
    #     j = remain // y
    #     curS = str(x) * i + str(y) * j
    #     num = int("".join(sorted(curS, reverse= True)))
    #     i += 1
    #     if num > ans:
    #       ans = num
    

    if x > y:
      x, y = y, x
    assert y > 0

    for cntY in range(n // y + 1):
      if (n - cntY * y) % x == 0:
        cntX = (n - cntY * y) // x

        ans = 0
        for i in range(cntY):
          ans = ans * 10 + y
        for i in range(cntX):
          ans = ans * 10 + x
        return ans

    return ans

sl = Solution()
print(sl.getMaxLuckyNumber(3, 4, 13))