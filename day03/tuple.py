# A Tuple is a list that can't be changed
# Write tuple with round breckets

# t = 3, 4
# print(type(t))

# def min_max(xs):
#     return min(xs), max(xs)

# for name, age in [("Asha", 28), ["Ravi", 25]]:
#     print(name, "is", age)

from collections import namedtuple
Person = namedtuple("Person", ["name", "age", "city"])
p = Person("Asha", 28, "Pune")
print(p.name)
print(p[1])