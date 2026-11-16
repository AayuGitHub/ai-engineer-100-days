import dis

def cal(a, b, c):
    total = (a + b) * c
    return total

print(cal(1, 2, 3))
dis.dis(cal)

"""
0 RESUME                   0 -> It started new process
2 LOAD_FAST                0 (a) -> It loaded a in memory
4 LOAD_FAST                1 (b) -> It loaded b nin memory
6 BINARY_OP                0 (+) -> It did binary operation (+)
10 LOAD_FAST                2 (c) -> It loaded c in memory
12 BINARY_OP                5 (*) -> It dud binary operation (*)
16 STORE_FAST               3 (total) -> It stored calculation in total
18 LOAD_FAST                3 (total) -> It loaded calculation in total
"""