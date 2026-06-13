class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        pointer = len(nums)//2
        while left <= right :
            pointer = left + (right - left)//2
            if nums[pointer] == target:
                return pointer
            elif target < nums[pointer]:
                right = pointer - 1
            else:
                left = pointer +1
                
        return -1


    



    
        