class Stack:
    def __init__(self):
        self.list = []
    def push (self, value):
        self.list.append(value)
    def size(self) -> int:
        return len(self.list)
    def pop(self) -> str:
        return self.list.pop()
    def peek(self) -> str:
        return self.list[-1]
    def isEmpty(self) -> bool:
        return len(self.list) == 0
    def clear(self):
        self.list.clear()

