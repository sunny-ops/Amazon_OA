from typing import *

class Solution:
    def solve(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Replace this with your solution
        ans = []
        allEdges = [] # (u, v, w, idx)
        idx = 0
        nodes = set()
        for u, v, w in edges:
            allEdges.append((u, v, w, -1))
            nodes.add(u)
            nodes.add(v)

        for u, v, w in queries:
            allEdges.append((u, v, w, idx))
            idx += 1
            nodes.add(u)
            nodes.add(v)

        allEdges.sort(key = lambda x: x[2])
        # print("allEdges", allEdges)
        parent = dict()
        for node in nodes:
            parent[node] = node

        def find(u):
            if parent[u] == u:
                return u
            parent[u] = find(parent[u])
            return parent[u]
        
        def union(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
        for u, v, w, idx in allEdges:
            if idx == -1:
                union(u, v)
            else:
                if find(u) == find(v):
                    ans.append((False, idx))
                else:
                    ans.append((True, idx))
        
        ans.sort(key = lambda x: x[1])
        return [bool for bool, idx in ans]


# N, M, Q = map(int, input().split())

edges = []
# for i in range(M):
#     a, b, c = map(int, input().split())
#     edges.append([a, b, c])


queries = []
# for i in range(Q):
#     u, v, w = map(int, input().split())
#     queries.append([u, v, w])

# edges = [[1,2,2], [1,3,6], [2,3,3], [3,5,8],[2,4,5],[4,5,9]]
# queries = [[1,3,1]]
# N = 5

# edges = [[5,6,3], [1,2,2], [2,3,3], [1,3,6],[2,4,5],[4,5,9],[3,5,8]]
# queries = [[1,3,1],[3,4,7],[3,5,7]]
# N = 5

edges = [[2,3,2],[1,2,100],[1,2,10000000000],[1,1,1]]
queries = [[1,2,2],[1,1,5]]
N = 3

s = Solution()

ansList = s.solve(N, edges, queries)

for ans in ansList:
    if ans:
        print("Yes")
    else:
        print("No")