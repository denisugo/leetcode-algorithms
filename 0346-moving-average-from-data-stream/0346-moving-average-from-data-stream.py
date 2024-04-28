class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.sum = 0
        self.len = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.len += 1

        substractor = 0
        if self.len > self.size:
            substractor = self.queue.popleft()
            self.len -= 1

        self.sum = self.sum - substractor + val

        return self.sum / self.len

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)