class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #the logic here is to see he entire matrix as one list for binary search
        m = len(matrix)#how many rows
        n = len(matrix[0])#how many columns

        left = 0
        right = m * n - 1 #the index of the last number if the matrix is converted to a single list

        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // n][mid % n]

            if val == target:
                return True
            elif val < target:
                left = mid + 1 #since already confirmed that list[mid] < target
            else:
                right = mid - 1
        
        return False