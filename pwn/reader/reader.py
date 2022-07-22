from pwn import *

#init

e = ELF('./ctemplate')
libc = ELF('./libcs-2.31.so')

p = process(e.path)
#p = remote()

#funcs

def add(x, y):
    p.sendlineafter('?', '1')
    p.sendlineafter('?', str(x))
    p.sendlineafter('?', str(y))

def fre(x):
    p.sendlineafter('?', '2')
    p.sendlineafter('?', str(x))

def chg(x, s = b''):
    p.sendlineafter('?', '3')
    p.sendlineafter('?', str(x))
    p.sendlineafter('?', s)

def rd(x):
    p.sendlineafter('?', '4')
    p.sendlineafter('?', str(x))
    p.recvuntil(': ')
    return p.recvline(keepends = False)

def ex():
    p.sendlineafter('?', '5')

#vars

#exploit

add(0, 0x18)
chg(0, 'asdf')
print(rd(0))
fre(0)
ex()

#pray for flag

p.interactive()
