from random import randint

class StringStack:
    def __init__(self, data):
        self.data = []

    def push(self, value):
        if not isinstance(value, str):
            raise TypeError("Only strings can appended to StringStack")
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(self.data[::-1])}]"


ss = StringStack()
[ss.push(str(randint(0, 100))) for _ in range(15)]
print(ss)
print(ss.pop())
print(ss.peek())
print(ss.is_empty())
print(ss)