class Glass:
    initial_content = 0
    capacity = 250
    def __init__(self):
        self.content = self.initial_content

    def fill(self, ml):
        left_space = self.get_left_capacity()
        if left_space >= ml:
            self.content += ml
            return f"Glass filled with {ml} ml"

        return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        left_space = self.get_left_capacity()
        return f"{self.capacity - self.content} ml left"

    def get_left_capacity(self):
        left_capacity = self.capacity - self.content
        return left_capacity


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
