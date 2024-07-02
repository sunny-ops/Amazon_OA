from functools import *
class Solution:
   def isRegexMatching(self, regex, arr):


       @cache
       def match(regex, s):
           # print(regex, s)
           # Edge cases
           if regex == ".*":
               return True
           if regex == "" and s == "":
               return True
           if regex == "" and s != "":
               return False


           # Special cases
           if regex.startswith("()*"):
               return match(regex[3:], s)
           if len(regex) >= 2 and regex[1] == '*':
               # Try to reuse the "regex[0] == '('" case to handle *
               return match('(' + regex[0] + ')*' + regex[2:], s)


           # Main body
           if regex[0] == '(':
               idx = regex.index(')*')
               assert (idx >= 0)
               sub_regex, res_regex = regex[1:idx], regex[idx + 2:]
               prefix_prefix = ""
               while len(prefix_prefix) <= len(s) and match(prefix_prefix, s[:len(prefix_prefix)]):
                   if match(res_regex, s[len(prefix_prefix):]):
                       return True
                   prefix_prefix += sub_regex
               return False
           elif regex[0] == '.':
               return s and match(regex[1:], s[1:])
           else:
               assert 'a' <= regex[0] <= 'z'
               return s and regex[0] == s[0] and match(regex[1:], s[1:])


       ans = [match(regex, s) for s in arr]
       return ans




solution = Solution()


print(solution.isRegexMatching("ab(e.r)*e", ["abbeere", "abefretre"]))
print(solution.isRegexMatching("..()*e*", ["abbeere", "abefretre"]))
print(solution.isRegexMatching("..()*e*", ["code", "abeee", "cd"]))