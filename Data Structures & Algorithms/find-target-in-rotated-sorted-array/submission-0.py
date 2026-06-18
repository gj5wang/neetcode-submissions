class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        #logic is that u try to find which group the target belongs to
        #on the left side or the right side

        while(left <= right):
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            #left half is sorted
            if nums[left] <= nums[mid]: #left half is sorted
                #target lies in left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            #right half is sorted
            else:
                #target lies in right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1



        




        