class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rec = 0
        height = 0
        max_height = max(heights)
        while height <= max_height:
            height += 1
            # print(f"height{height}")

            save = []
            for i in range(len(heights)):
                if heights[i] < height:
                    save.append(i)
            # print(f"save{save}")
            start = 0
            width = 0
            if len(save) == 0:
                width = len(heights)
            else:
                for i in save:
                    width = max(i-start, width)
                    start = i+1
                width = max(len(heights)- start, width)
            max_rec = max(height * width, max_rec)
            # print(f"max_rec{max_rec}")

            
        return max_rec
            
        