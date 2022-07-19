import binascii;

# print(len(bin(int(binascii.hexlify(open("flag.txt").read().encode("ascii")),16))) - 2);
print(bin(int(binascii.hexlify(open("flag.txt").read().encode("ascii")),16)));