class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        if s == "":
            return 0
        string = [s[0]]
        max_total =1
        # for i in range(len(s)):
        #     if s[i] in []:
        #         max_total = len(string)
        #         right = i
        #         left =1
        #         del s[0]
        #         break
        #     else:
        #         string.append(i)
        while right < len(s)-1:
            print(f"{string} number{max_total}")

            right += 1
            if s[right] not in string:
                string.append(s[right])
                max_total = max(max_total, len(string))

            else:
                while s[right] in string:
                    left += 1
                    del string[0]
                string.append(s[right])
        return max_total
               





        

        
        