# Last updated: 08/12/2025, 22:31:52
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        max_sub = nums[0]
4        curr = 0
5        for i in nums:
6            if curr < 0:
7                curr = 0
8            curr += i
9            max_sub = max(max_sub, curr)
10        return max_sub