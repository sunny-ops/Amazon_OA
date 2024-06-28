class Solution:
  def orderedConfiguration(self, configuration: str):
    configs = set()
    
    arr = configuration.split("|")
    arr.sort()
    print(arr)
    ans = []
    lastIdx = 0
    for i in range(len(arr)):
      if int(arr[i][:4]) != lastIdx + 1:
        print(int(arr[i][:4]))
        print("hhh1")
        return ["Invalid configuration"]
      if arr[i][4:] in configs:
        print("hhh2")
        return ["Invalid configuration"]
      ans.append(arr[i][4:])
      lastIdx += 1
      configs.add(arr[i][4:])
    
    return ans

sl = Solution()
print(sl.orderedConfiguration("0001LAJ5KBX9H8|0003UKURNK403F|0002MO6K1Z9WFA|0004OWRXZFMS2C"))