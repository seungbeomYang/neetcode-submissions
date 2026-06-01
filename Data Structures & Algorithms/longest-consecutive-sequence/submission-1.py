class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_set = sorted(set(nums))
        print(sorted_set)
        if len(sorted_set) == 0:
            return 0

        longest_seq = 0
        set_add = 1
        for index in range(1, len(sorted_set)):
            if sorted_set[index - 1]+1== sorted_set[index]:
                set_add += 1
            else:
                if set_add >= longest_seq:
                    longest_seq = set_add
                    set_add = 1
        if longest_seq < set_add:
            longest_seq = set_add
            
        return longest_seq
        

        