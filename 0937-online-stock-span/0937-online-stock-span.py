class StockSpanner:

    def __init__(self):
        self.stack = []  # price, day_count

    def next(self, price: int) -> int:
        day_count = 1
        while self.stack and not price < self.stack[-1][0]:
            day_count += self.stack.pop()[1]

        self.stack.append((price, day_count))

        return day_count