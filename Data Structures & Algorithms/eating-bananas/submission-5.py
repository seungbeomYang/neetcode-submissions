class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def find_hour(k: int) -> int:
            count = 0
            for pile in piles:
                count += (pile + k - 1) // k
            return count
        index = 0
        remainder = h

        min_val = 1
        max_val = max(piles)


        while min_val <= max_val:
            middle_val = min_val + (max_val-min_val)//2 
            value = find_hour(middle_val)
            if h < value:
                min_val = middle_val + 1
                
            else:
                max_val = middle_val -1
        return min_val



        