from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums: List[int] = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(max(nums[i], sums[i-1]+nums[i]))
        return max(sums)


s = Solution()
print(s.maxSubArray([1, 12, 3, 4, 1, 23, 1, 2]))
