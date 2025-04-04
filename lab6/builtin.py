#task 1
def multiplyList(a):
    res = 1
    for i in a:
        res*=i
    return res

lst = [2,3,4,5]
print(multiplyList(lst))

#task 2
def uplownum(s):
    up = 0
    low = 0
    for i in s:
        if ord(i) > 96:
            low+=1
        else:
            up += 1
    return up,low

print(uplownum("ADHsdfjsSd"))

#task 3
def isPolindrom(s):
    return s == s[::-1]

print(isPolindrom("kazak"))

#task 4
import time

def squar(n, t):
    time.sleep(t/1000)
    return n**0.5

print(squar(25100, 2123))

#task 5
def allTrue(t):
    return all(t)

print(allTrue((1,1,1)))