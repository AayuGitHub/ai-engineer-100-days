import copy
original = [[1, 2], [3,4]]
alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

original[0].append(99)
original.append([5]) 
print("original: ") 
print(original) 

print("alias: ")
print(alias)
print("alias is original: ")

print("shallow: ")
print(shallow)
print("shallow is original: ")
print(shallow is original)

print("deep: ")
print(deep)
print("deep is original: ")
print(deep is original)