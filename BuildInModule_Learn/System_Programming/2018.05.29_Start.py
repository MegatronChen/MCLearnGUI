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