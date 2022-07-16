answers = [
    2,
    4,
    240,
    3,
    165580141,
    10,
    5838215,
    111222345,
    543222111,
    9
]

with open("flag.txt") as f:
    flags = f.readlines()[0].strip()
    flag = [ord(i) for i in flags]
    for i in answers:
        for j in range(len(flag)):
            flag[j] ^= ((i^0x94d049bb133111eb) * (j^0xbf58476d1ce4e5b9)) & 0xffffffffffffffff;
    for i in flag:
        print(str(i) + "U,")
    print(len(flag))

