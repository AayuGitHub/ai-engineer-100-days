# Lists
a = [1, 2]
b = a
b.append(3)
print(a)
print(b)
print(id(a))
print(id(b))

# Comment: Object wasn't changed and append makes changes in runtime so b and a both gets 3 and it still points to same obj id.

# Ints

a = 10
b = a
b = b + 1
print(a)
print(b)
print(id(a))
print(id(b))

# Comment: Object was changed when we added 1 to b until then it was same and when we do b + 1; it creates new object so new ID!

# strings

a = "hi"
b = a
b += "!"
print(a)
print(b)
print(id(a))
print(id(b))

# Comment: Object was changed when we added ! to b and when we do +=; it creates new object so new ID!
