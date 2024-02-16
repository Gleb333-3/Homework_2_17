class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        return f"{self.name} is {self.age}"
a = Person('Bob', 12)
print(a.get_info())