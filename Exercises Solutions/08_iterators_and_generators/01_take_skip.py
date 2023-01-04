class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.count * self.step:
            raise StopIteration
        count = self.current
        self.current += self.step
        return count


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
