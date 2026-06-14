class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in lst:
                            lst.append(triplet)
        return lst

        