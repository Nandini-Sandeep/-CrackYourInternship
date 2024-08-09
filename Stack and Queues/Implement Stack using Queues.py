class MyStack:

    def __init__(self):
        self.q1 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        q = self.q1[:-1]
        ans = self.q1[-1]
        self.q1 = q
        return ans

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return self.q1==[]
