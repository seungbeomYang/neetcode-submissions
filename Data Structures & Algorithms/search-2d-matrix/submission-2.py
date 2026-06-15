class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        right = len(matrix)-1
        pointer = len(matrix)//2
        target_list = []
        while left <= right:
            pointer = left + (right - left)//2
            print(matrix[pointer])
            if matrix[pointer][0] <= target <= matrix[pointer][len(matrix[pointer])-1]:
                target_list = matrix[pointer]
                if target in matrix[pointer]:
                    return True
                else:
                    return False
            elif matrix[pointer][0] > target:
                right = pointer-1
            else:
                left = pointer +1
        return False
            
        

        
        