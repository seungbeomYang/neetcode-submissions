class MinStack:

    def __init__(self):
        self.whatever = []
        self.minn =21474836470
        

    def push(self, val: int) -> None:
        if not self.whatever:
            current_min = val
        else:
            current_min = min(val, self.whatever[-1][1])
        self.whatever.append((val,current_min))
        

    def pop(self) -> None:
        self.whatever.pop()
        

    def top(self) -> int:
        return self.whatever[len(self.whatever)-1][0]
        

    def getMin(self) -> int:
        return self.whatever[len(self.whatever)-1][1]
        
        
