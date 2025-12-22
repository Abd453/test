# Last updated: 22/12/2025, 23:05:31
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        dic = {'I': 1,'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
4
5        result = 0
6        for key, value in enumerate(s):
7            if key + 1 < len(s) and dic[value] < dic[s[key+1]]:
8                result -= dic[value]
9            else:
10                result += dic[value]
11        return result
12        
13       