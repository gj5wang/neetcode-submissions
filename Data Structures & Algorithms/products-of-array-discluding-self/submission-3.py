class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_cnt = 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        if zero_cnt > 1: return [0] * len(nums) #if theres more than 2 zeros then no matter what every element is an zero

        res = [0] * len(nums)
        for i, c in enumerate(nums): #gives index and item
        #if one zero, the index with zero gets prod, all others get 0
            if zero_cnt == 1:
                if c == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                #no zeros, remove current number from the product
                res[i] = int(prod/nums[i])
        return res