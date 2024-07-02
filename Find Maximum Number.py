class Solution:
  def findMaximumNum(self, answered, needed, q: int):
    additional_needed = [needed[i] - answered[i] for i in range(len(answered))]
    
    # 按照所需的额外题目数量从小到大排序
    additional_needed.sort()
    print(additional_needed)
    
    # 初始化通过的科目数量
    passed_subjects = 0
    
    # 分配题目
    for extra in additional_needed:
        print("extra", extra)
        if q >= extra:
            q -= extra
            passed_subjects += 1
        else:
            break
    
    return passed_subjects

sl = Solution()
print(sl.findMaximumNum([24, 27, 0], [51, 52, 100], 100))