# 232. Implement Queue using Stacks

from collections import deque

class MyQueue:
    def __init__(self):
        self.stack_in = deque()
        self.stack_out = deque()

    def push(self, x: int) -> None:
        self.stack_in.appendleft(x)

    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                val = self.stack_in.popleft()
                self.stack_out.appendleft(val)
        return self.stack_out.popleft()

    def peek(self) -> int:
        val = self.pop()  # reuse pop() method in this class for null out stack check
        self.stack_out.appendleft(val)  # add it back
        return val

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()