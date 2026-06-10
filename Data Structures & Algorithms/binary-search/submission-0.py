class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 #no need for int inthe front
        right = len(nums) - 1

        while(left <= right) :
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                    left += 1
            elif nums[mid] > target:
                    right -= 1
             

        return -1