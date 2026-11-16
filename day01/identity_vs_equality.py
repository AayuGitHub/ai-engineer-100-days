# Two separate lists with equal values: compare them with == and with is.
list_a = [1, 2, 3, 4]

list_b = [1, 2, 3, 4]

print(f"ID of List A: ", id(list_a))
print(f"ID of List B: ", id(list_b))

if list_a == list_b:
    print("Matched")

if list_a is list_b:
    print("Matched")

# A None check written the correct way.

value = None
if value is None:
    print("No value")
if value is not None:
    print("Value exists:", value)

"""
Small ints: x = 256; y = 256 and x = 257; y = 257, comparing with is each time.
Hint: run the 257 test twice, once typed line by line in the REPL and once inside your script. If the results differ, write down why in a comment. That’s an important discovery; don’t look it up until you’ve noticed it yourself.
"""

x = 256
y = 256
print(x is y)
print(id(x), id(y))
x = 257
y = 257
print(x is y)
print(id(x), id(y))

# Comment: when I ran above block of code in REPL; first print came true but not the second one and when I checked IDs of x and y both times then in 256 one, x and y had same IDs but that wasn't case with 257 and so for 257 came False as is matches ID instead of value! but when I ran same block of code in file then both came true and because Ids were same for X and Y for both 256 and 257 instances so that it came true as is matches ID and not value!


"""
When to use "is":
- when we want IDs to be compared and not just when we want to compare values

When to use "==":
- when we want to compare two values with each other exactly!
"""
