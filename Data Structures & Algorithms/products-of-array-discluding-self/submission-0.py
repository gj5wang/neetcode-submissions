class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        for i in range(0, len(nums)):
            out = 1
            for m in range(len(nums)):
                if m != i: 
                #skip current index
                    out *= nums[m]
            
            product.append(out)
        return product