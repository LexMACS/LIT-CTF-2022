with open("output", "rb") as f:
    x = f.read()
    print("\"", end="")
    for i in range(0, len(x)):
        c = x[i]
        print("\\" + hex(c)[1:], end="")
        if (i+1) % 50 == 0:
            print("\"\n\"", end="")
    print("\"")
    print("LEN: " + str(len(x)))
