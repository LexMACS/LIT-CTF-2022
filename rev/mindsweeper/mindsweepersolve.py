from pwn import *
from z3 import *
import time

start = time.time()

p = remote("34.162.151.17", 30001)

n = 32

seed = BitVec('seed', 64)
seeds = [BitVec('seed' + str(i), 64) for i in range(n+1)]

s = Solver()

s.add(seeds[0] == ((seed ^ 0x5DEECE66D) & ((1 << 48) - 1)))

for i in range(n):
    s.add(seeds[i+1] == ((seeds[i] * 0x5DEECE66D + 0xB) & ((1<<48)-1)))

log.info(p.recvlineS())
log.info(p.recvlineS())

raw_b = p.recvuntilS("\nEnter", drop=True)
log.info(raw_b)

a = raw_b.split("\n")

b = [[0 for i in range(32)] for j in range(n)]

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == '?':
            continue
        v = 0
        if a[i][j] == '*':
            v = 1
        b[j][i] = 1
        s.add(v == ((seeds[j+1] >> (16 + i)) & 1))

log.info("Is it sat???? " + str(s.check()))

m = s.model()
seed = m[seed].as_long()
log.info("Seed: " + str(seed))

log.info("Time elapsed: " + str(round(time.time() - start, 2)))

cur_seed = ((seed ^ 0x5DEECE66D) & ((1 << 48) - 1))
for i in range(n):
    cur_seed = ((cur_seed * 0x5DEECE66D + 0xB) & ((1<<48)-1))
    cur_int = cur_seed >> 16
    for j in range(32):
        if b[i][j]:
            continue
        if ((cur_int >> j) & 1) == 1:
            p.sendline(("mine " + str(i) + " " + str(j)).encode())
        else:
            p.sendline(("clear " + str(i) + " " + str(j)).encode())

p.recvuntil("I don't know how you did it, but you won!", drop=True)
p.interactive()
