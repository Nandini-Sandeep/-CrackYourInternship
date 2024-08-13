# The idea is to start two stacks from two extreme corners of arr[].
# stack1 starts from the leftmost element, the first element in stack1 is
# pushed at index 0. The stack2 starts from the rightmost corner, the first
# element in stack2 is pushed at index (n-1). Both stacks grow (or shrink)
# in opposite direction. To check for overflow, all we need to check is for
# space between top elements of both stacks.


class TwoStacks:

    def __init__(self, n=100):
        # Size of the array
        self.size = n

        # Array to store elements
        self.arr = [0] * n

        # Top index of stack 1
        self.top1 = -1

        # Top index of stack 2
        self.top2 = n

    # Function to push an integer into stack 1
    def push1(self, x):
        # If there is space between the top of both stacks,
        # we push the element at top1+1.
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x

    # Function to push an integer into stack 2
    def push2(self, x):
        # If there is space between the top of both stacks,
        # we push the element at top2-1.
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x

    # Function to remove an element from top of stack 1
    def pop1(self):
        # If top1 == -1, stack1 is empty so we return -1,
        # else we return the top element of stack1.
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            return -1

    # Function to remove an element from top of stack 2
    def pop2(self):
        # If top2 == size of array, stack2 is empty so we return -1,
        # else we return the top element of stack2.
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            return -1
