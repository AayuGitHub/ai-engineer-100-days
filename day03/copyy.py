from copy import deepcopy

# team = [["Asha", 90], ["Ravi", 80]]
# backup = team.copy()
# print(f"Team: {team}")
# print(f"Backup: {backup}")
# backup[0][1] = 0
# print(team)

# safe = deepcopy(team)
# safe[1][1] = 0
# print(f"Safe: {safe}")
# print(f"Team: {team}")

a = [[1], [2]]
b = a
c = a.copy()
d = deepcopy(a)
a[0].append(9)
print(b[0], c[0], d[0])
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(b is a, c is a, c[0] is a[0], d[0] is a[0])
