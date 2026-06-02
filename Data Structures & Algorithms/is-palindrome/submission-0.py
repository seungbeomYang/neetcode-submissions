class Solution:
    def isPalindrome(self, s: str) -> bool:
        word_list = [char.lower() for char in s if char.isalnum()]
        print(word_list)
        print(len(word_list)//2)
        # if len(word_list)//2 != 0:
        #     return False
        for index in range(round(len(word_list)/2)):
            if word_list[index] != word_list[len(word_list)-index-1]:
                return False
            else:
                print(f"{word_list[index]} == {word_list[len(word_list)-index-1]}")
        return True
        
        