class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current_idx = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:

            if self.current_idx == len(self.sequence):
                self.current_idx = 0

            self.current_idx += 1
            self.counter += 1
            return self.sequence[self.current_idx - 1]
        raise StopIteration


result = sequence_repeat("123456", 12)
for item in result:
    print(item, end='')
