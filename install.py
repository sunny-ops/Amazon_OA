####
from collections import deque
from collections import Counter
class Solution:
    def __init__(self):
        self.s = Counter()
        
        
            
    def install(self, map, a):
        # dfs
        def dfs(node):
            if self.s[node] > 0:
                return
            #    print("node", node)
            for neighbor in map[node]:
                dfs(neighbor)
                self.s[neighbor] += 1
            print("node", node)
        
        dfs(a)
    
    def uninstall(self, map, a):
        ans = []
        queue = deque()
        queue.append(a)
        while queue:
            node = queue.popleft()
            ans.append(node)
            del self.s[node]
            print("s", self.s)
            for neighbor in map[node]:
                self.s[neighbor] -= 1
                if self.s[neighbor] == 0:
                    queue.append(neighbor)
        print("ans", ans)

       


sl = Solution()
map = dict()
map['alpha'] = ["bravo", "charlie"]
map["bravo"] = ["delta"]
map["charlie"] = ["bravo"]
map["delta"] = []
map["echo"] = ["bravo"]
map["foxtrot"] = []
sl.install(map, "alpha")
print("here", sl.s)
sl.uninstall(map, "alpha")
print(sl.s)
