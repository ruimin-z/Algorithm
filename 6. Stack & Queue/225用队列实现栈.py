# 225. Implement Stack using Queues

from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        # if not self.q: return -1
        for _ in range(1, len(self.q)):  # rotate len-1 times
            self.q.append(self.q.popleft())  # get front, append to end
        return self.q.popleft()

    def top(self) -> int:  # Returns the element on the top of the stack.
        val = self.pop()  # reuse
        self.q.append(val)
        return val

    def empty(self) -> bool:
        return not self.q

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()