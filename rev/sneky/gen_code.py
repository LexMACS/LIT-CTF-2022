import random

def popcnt(i):
    return bin(i).count('1');

funcs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fname = ["mul", "eq", "add1", "mov1", "mov2", "mod", "out", "add0", "inp", "mov0"]

with open("assembly") as f:
    lns = f.readlines()
    lz = [i.strip() for i in lns]
    with open("output", "wb") as fw:
        for l in lz:
            s = l.split()
            if len(s) == 0: continue
            op = -1
            print(s)
            for i in range(len(fname)):
                if fname[i] == s[0]:
                    op = i
                    break
            funcuse = -1
            while funcuse == -1:
                for i in range(len(funcs)):
                    if funcs[i] == op and random.random() < 0.7:
                        funcuse = i
                        break
                if funcuse == -1:
                    cx = random.randint(0, 9)
                    funcs[cx] += 1
                    funcs[cx] %= 10
                    opcode = cx
                    data = random.randint(0, (1<<12)-1)
                    if (popcnt(data) & 1) == 1:
                        data ^= 1
                    instruction = (opcode << 12) | data
                    #print(bin(instruction))
                    fw.write(instruction.to_bytes(2, "big"))
            dat1 = int(s[1])
            dat2 = 0
            if len(s) > 2:
                dat2 = int(s[2])
            dat = (dat1 << 9) | dat2
            if (popcnt(dat) & 1) != 1:
                dat |= (1<<8)
            inst = (funcuse << 12) | dat
            fw.write(inst.to_bytes(2, "big"))
            funcs[funcuse] += 1
            funcs[funcuse] %= 10


