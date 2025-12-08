# Last updated: 08/12/2025, 22:16:57
1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3        if not nums:
4            return []
5        sum = 0
6        for i in range(len(nums)):
7            sum += nums[i]
8            nums[i] = sum
9        return nums