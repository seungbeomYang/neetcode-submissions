class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sorted_list = sorted(nums)
        pointer = 0
        
        while pointer  < len(nums)-2 :
            pl = pointer + 1
            pr = len(nums)-1
            while pl < pr:
                if (sorted_list[pointer] + sorted_list[pl] + sorted_list[pr]) > 0:
                    pr -= 1
                elif (sorted_list[pointer] + sorted_list[pl] + sorted_list[pr]) < 0:
                    pl += 1
                else:
                    output.append([sorted_list[pointer], sorted_list[pl], sorted_list[pr]])
                    pl += 1
                    pr -= 1

                    while pl < pr and sorted_list[pl] == sorted_list[pl - 1]:
                        pl += 1

                    while pl < pr and sorted_list[pr] == sorted_list[pr + 1]:
                        pr -= 1
            if (pointer + 1) < len(nums):
                while pointer + 1 < len(nums) and sorted_list[pointer+1] == sorted_list[pointer]:
                    pointer += 1
            pointer += 1
        return output

                
                
                


        