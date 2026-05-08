class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_list = []
        for index in range(len(nums)):
            result = 1
            for i, value in enumerate(nums):
                if i == index:
                    continue
                else:
                    result *= value
            result_list.append(result)
        return result_list
            
                