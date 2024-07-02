from collections import Counter
class Solution:
  def countFaults(self, n: int, logs):
    ans = 0
    c = Counter()
    for log in logs:
      server, res = log.split(" ")
      if res == "success":
        continue
      else:
        c[server] += 1
        if c[server] == 3:
          ans += 1
          c[server] = 0

    return ans
  
sl = Solution()
print(sl.countFaults(2, ["s1 error", "s1 error", "s2 error", "s1 error", "s1 error", "s2 success"]))