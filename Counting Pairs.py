from collections import Counter
class Solution:
  def countPairs(self, numbers, k: int):
    c = Counter(numbers)
    print("c,", c)
    if k == 0:
      return len(c)
    s = set()
    cnt = 0
    for key in c.keys():
      find = key - k
      if find in s:
        cnt += 1
      s.add(key)
    return cnt

sl = Solution()
print(sl.countPairs([1, 1, 1, 2], 1))
print(sl.countPairs([1, 2], 0))