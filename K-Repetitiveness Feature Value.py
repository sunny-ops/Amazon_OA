from collections import Counter
class Solution:
  def getkRepValue(self, user_history: str, k: int):
    cnt = 0
    l = 0
    c = Counter()
    for r in range(len(user_history)):
      c[user_history[r]] += 1
      while max(c.values()) >= k:
        c[user_history[l]] -= 1
        l += 1
      # [l, r] is the shortest invalid ending at r
      cnt += l
    return cnt

sl = Solution()
print(sl.getkRepValue("ceccca", 3))