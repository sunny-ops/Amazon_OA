class Solution:
  def reduceGifts(self, prices, k: int, threshold: int) -> int:
    n = len(prices)
    if len(prices) < k:
      return 0
    prices.sort()
    total = sum(prices[:k])
    if total > threshold:
      return n - (k - 1)
    for i in range(k, n):
      total -= prices[i - k]
      total += prices[i]
      if total > threshold:
        idx = i
        break
    return n - 1 - idx + 1

sl = Solution()
print(sl.reduceGifts([3, 2, 1, 4, 6, 5], 3, 14))
print(sl.reduceGifts([9, 6, 7, 2, 7, 2], 2, 13))
print(sl.reduceGifts([9, 6, 3, 2, 9, 10, 10, 11], 4, 1))
