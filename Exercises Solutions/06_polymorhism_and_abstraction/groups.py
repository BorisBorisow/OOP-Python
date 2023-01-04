class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        name = f"{self.name} {self.surname}"
        return name

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        length_of_group = len(self.people)
        return length_of_group

    def __add__(self, other):
        new_name = f"{self.name} {other.name}"
        merged_groups = self.people + other.people
        return Group(new_name, merged_groups)

    def __str__(self):
        members_names_str = ", ".join(str(p) for p in self.people)
        return f"Group {self.name} with members {members_names_str}"

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index]}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
