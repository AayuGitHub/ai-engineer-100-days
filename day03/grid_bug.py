# grid = [[0] * 3] * 3
# print(grid)
# grid[0][0] = 1
# print(grid)
# print(grid[0] is grid[1])

grid = []

for i in range(3):
    grid.append([0] * 3)

print(f"Before Modification: {grid}")

grid[0][0] = 1

print(f"After Modification: {grid}")

print("\nAre rows the same object?", grid[0] is grid[1])

# The * operator repeats references to the same inner list instead of creating new lists.
# Therefore, modifying one row also changes the other rows.