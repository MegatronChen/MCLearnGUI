# 《Programming Python》系统编程部分
# 始于2018.05.29

# Chapter2

# import sys,os
# help(dir)
# print(len(dir(os.path)))
# help(input)

# import more
# help(more)

# import sys
# print(sys.platform)
# if sys.platform[:3] == 'win':print('hello windows')
# print(sys.path)
# print(sys.exc_info())

# import os
# help(os.environ)
# print(os.getcwd())
# print(list(os.environ))
#
# import sys
# for f in (sys.stdin,sys.stdout,sys.stderr):
#     print(f)

#
# from subprocess import Popen,PIPE,call
# X = call('python hello-out.py')
# print(X)

# print(open('hello-in.txt','rb').read())

# data = 'sp\xe4m'
# # print(data)
# # print(0xe4,bin(0xe4),chr(0xe4))
# print(data.encode('latin1'))
# print(data.encode('utf8'))
# print(data.encode('utf16'))
# print(data.encode('cp500'))


# import struct
# data = struct.pack('>i4shf', 2  ,'spam' , 3 , 1.234)
# print(data)



# Chapter5
# 2018.06.13

# Example5.1
#
import os
# # help(os.fork)
#
# def child():
#     print('hello from child',os.getpid())
#     os._exit(0)
#
# def parent():
#     while True:
#         newpid = os.fork()
#         if newpid == 0:
#             child()
#         else:
#             print('hello from parent',os.getpid(),newpid)
#         if input() == 'q':
#             break
#
# parent()


# # Example5.2
# import os,time
# def counter(count):
#     for i in range(count):
#         time.sleep(1)
#         print('[%s] => %s' % (os.getpid(),i))
#
# for i in range(5):
#     pid = os.fork()
#     if pid != 0:
#         print('Process %d spawned' % pid)
#     else:
#         counter(5)
#         os._exit(0)
#
# print('Main process exiting')


# # Example5.3
# import os
# # help(os.fork)
#
# parm = 0
# while True:
#     parm += 1
#     pid = os.fork()
#     if pid == 0:
#         os.execlp('python','python','child.py',str(parm))
#         assert False,'error starting program'
#     else:
#         print('Child is',pid)
#         if input() == 'q':break


# # Example5.5
# import _thread
#
# def child(tid):
#     print('Hello from thread',tid)
#
# def parent():
#     i = 0
#     while True:
#         i += 1
#         _thread.start_new_thread(child,(i,))
#         if input() == 'q':
#             break
#
# parent()


# # Example5.5-2
# import _thread
#
# def action(i):
#     print(i**32)
#
# class Power:
#     def __init__(self,i):
#         self.i = i
#     def action(self):
#         print(self.i**32)
#
# _thread.start_new_thread(action,(2,))
#
# _thread.start_new_thread((lambda : action(2)),())
#
# obj = Power(2)
# _thread.start_new_thread(obj.action,())


# # Example5.6
# import _thread as thread,time
#
# def counter(myID,count):
#     for i in range(count):
#         time.sleep(1)
#         print('[%s] => %s'% (myID,i))
#
# for i in range(5):
#     thread.start_new_thread(counter,(i,5))
#     time.sleep(6)
#     print('Main thread exiting.')


# # Example5.7
# import _thread as thread
# stdoutmutex = thread.allocate_lock()
# exitmutexs = [thread.allocate_lock() for i in range(10)]
#
# def counter(myID,count):
#     for i in range(count):
#         stdoutmutex.acquire()
#         print('[%s] => %s' % (myID, i))
#         stdoutmutex.release()
#     exitmutexs[myID].acquire()
#
# for i in range(10):
#     thread.start_new_thread(counter,(i,100))
#     for mutex in exitmutexs:
#         while not mutex.locked():
#             pass
#     print('Main thread exiting.')


# Example5.10
import _thread as thread,time

stdoutmutex = thread.allocate_lock()
numthreads = 5
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]

def counter(myID,count,mutex):
    for i in range(count):
        time.sleep(1/(myID+1))
        with mutex:
            print('[%s] => %s' % (myID, i))
    exitmutexes[myID].acquire()

for i in range(numthreads):
    thread.start_new_thread(counter,(i,5,stdoutmutex))

while not all(mutex.locked() for mutex in exitmutexes):time.sleep(0.25)
print('Main thread exiting.')