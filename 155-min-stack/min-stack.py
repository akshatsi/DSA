class MinStack:

    def __init__(self):
        self.s = []
        self.s_aux = []
    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.s_aux:
            self.s_aux.append(val)
        elif val <= self.s_aux[-1]:
            self.s_aux.append(val)
        else:
            self.s_aux.append(self.s_aux[-1])


    def pop(self) -> None:
        if not self.s:
            return
        self.s.pop()
        self.s_aux.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s_aux[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()