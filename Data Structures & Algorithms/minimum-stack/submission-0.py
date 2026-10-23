class MinStack:

    def __init__(self):
        self.minStack = []
        self.minimum=[]

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if self.minimum:
            self.minimum.append(min(val, self.minimum[-1]))
        else:
            self.minimum.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]