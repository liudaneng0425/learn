#!/usr/bin/env python
#coding=utf-8

print "Hello Fibonacci Sequence!"

import time

def fbis(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

def main():
    result = fbis(10)
    fobj = open('D:\\Users\\liudaneng\\eclipse-workspace\\ThefirstPythonPrj\\result.txt','w+')
    for i,num in enumerate(result):
        print u" 第 %d个数是 : %d" % (i,num)
        fobj.write("%d "%num)
        time.sleep(0.5)

if __name__ == '__main__':
    main()        