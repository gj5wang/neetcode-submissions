class Solution:
    def findMin(self, nums: List[int]) -> int:
        #find two sorted halves
        #the minimum is where the "break" occurs
        left = 0
        right = len(nums) - 1 

        while (left < right):
            mid = (left + right) // 2
            
            if nums[right] < nums[mid]: #only need to compare to nums[right]
                left = mid + 1
            else:
                right = mid

        return nums[left]
        
        
        