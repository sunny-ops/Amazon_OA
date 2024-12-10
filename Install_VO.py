# We are in charge of designing a system to install packages on computer systems.
# We are required to support the installation of a package and all of its dependent packages. 
# Here is an example of a package structure that we would need to install: 
#     A depends on B, C 
#     B depends on D, E, F
#     C depends on F, E 
#     F depends on G 
#     X depends on Y Z 
#     Z depends on X
#     R depends on T

# (1)
#     installation can be achieved once all dependent 
#     packages have been installed by calling sys.install('A') Dependencies can be found by calling repo.getDependencies('A') 
# => returns ['B', 'C'] In the above example, you are given a list of dependencies ['A', 'B', 'C', 'F']

visited = set()
def dfs(node):
    visited.add(node)
    for neighbor in repo.getDependencies(node):
        if neighbor not in visited:
            dfs(neighbor)
    sys.install(node)

Arr = ['A', 'B', 'C', 'F']
for ele in arr:
    if ele not in visited:
        dfs(ele)

# (2)
#  if C depends on A, F, E, there is a cycle in the dependency graph.
# In this case, the installation should fail and raise an exception.

# 1. use a stack to keep track of the current path
#  when visiting a node, push it to the stack, when leaving the node, pop it from the stack 
# instack 表示进栈了，但是还没做完，还没出栈 
visited = set()
instack = set()
def dfs(node):
    visited.add(node)
    instack.add(node)
    for neighbor in repo.getDependencies(node):
        if neighbor in instack:
            raise Exception("Cycle detected")
        if neighbor not in visited:
            dfs(neighbor)
    sys.install(node)
    instack.remove(node)

# 2. use a color to represent the state of the node
# 0: not visited, 1: visiting, 2: visited
color = Counter()
def dfs(node):
    color[node] = 1
    for neighbor in repo.getDependencies(node):
        if color[neighbor] == 1:
            raise Exception("Cycle detected")
        if color[neighbor] == 0:
            dfs(neighbor)
    sys.install(node)
    color[node] = 2