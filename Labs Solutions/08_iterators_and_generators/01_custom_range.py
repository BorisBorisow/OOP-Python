# class custom_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.current = self.start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         temp = self.current
#         self.current += 1
#         return temp
#
#
# for el in custom_range(1, 10):
#     print(el)


class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        temp = self.start
        self.start += 1
        return temp


for el in custom_range(1, 10):
    print(el)
