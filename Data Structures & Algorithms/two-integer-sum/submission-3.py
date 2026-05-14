class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (0, len(nums) - 1):
            for m in range (i + 1,len(nums)):
                if nums[i] + nums[m] == target:
                    return [i, m]