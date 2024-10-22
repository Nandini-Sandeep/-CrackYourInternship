class MyQueue:
    def __init__(self):
        self.S = []

    def push(self, x: int) -> None:
        self.S.append(x)

    def pop(self) -> int:
        return self.S.pop(0)

    def peek(self) -> int:
        return self.S[0]

    def empty(self) -> bool:
        return self.S==[]
