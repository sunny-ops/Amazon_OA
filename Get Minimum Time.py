class Solution:
  def getMinTime(self, total_servers: int, servers):
    servers.sort()
    servers = [servers[-1]] + servers
    n = len(servers)
    ans = 0
    for i in range(1, n - 2):
      ans += servers[i + 1] - servers[i]
    return ans + min(servers[-1] - servers[-2], total_servers + servers[1] - servers[0])
  
sl = Solution()
print(sl.getMinTime(8, [2, 6, 8]))
print(sl.getMinTime(10, [4, 6, 2, 9]))