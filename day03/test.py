import time

xs = []
start = time.perf_counter()
for i in range(50_000):
    xs.append(i)
print(f"append   : {time.perf_counter() - start:.4f} s")

ys = []
start = time.perf_counter()
for i in range(50_000):
    ys.insert(0, i)
print(f"insert(0): {time.perf_counter() - start:.4f} s")