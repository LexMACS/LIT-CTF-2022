import random

xor = []
ans = []

with open("flag.txt") as f:
    flag = f.readlines()[0].strip()[::-1]
    flen = len(flag)
    stack = list(flag + flag[flen-1])
    for i in range(flen):
        xor.append(random.randint(0, 127))
    for i in range(flen):
        r0 = stack[i]
        r1 = xor[i]
        r3 = stack[i+1]
        stack[i+1] = r0
        stack[i] = r3
        r0 = stack[i]
        r3 = ord(r0) ^ r1
        r2 = ~r3
        ans.append(r2)

print(xor[::-1])
print(ans[::-1])
