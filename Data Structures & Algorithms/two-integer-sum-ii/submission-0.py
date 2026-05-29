class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #find which number adds up to target using a for loop
        #only add the number on the right of the original number
        for i in range(1, len(numbers)):
            for m in range(i + 1, len(numbers) + 1):
                if numbers[i - 1] + numbers[m - 1] == target:
                    return [i, m]