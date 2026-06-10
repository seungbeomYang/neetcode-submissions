class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '{', '[', ]
        closing = [')', '}', ']']
        stack = []
        for i in s:
            if i in opening:
                stack.append(i)
            elif i in closing:
                if len(stack)>0 and stack[0] in opening:
                    character = stack.pop()
                    match character:
                        case '(':
                            if i != ')':
                                return False

                        case '[':
                            if i != ']':
                                return False
                        
                        case '{':
                            if i != '}':
                                return False
                else: 
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

        