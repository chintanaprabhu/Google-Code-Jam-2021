#Problem
#We have a list of integers X1,X2,…,XN. We would like them to be in strictly increasing order, but unfortunately, we cannot reorder them. This means that usual sorting algorithms will not work.

#Our only option is to change them by appending digits 0 through 9 to their right (in base 10). For example, if one of the integers is 10, you can turn it into 100 or 109 with a single append operation, or into 1034 with two operations (as seen in the image below).

#Given the current list, what is the minimum number of single digit append operations that are necessary for the list to be in strictly increasing order?

#Sample Input
#4
#3
#100 7 10
#2
#10 10
#3
#4 19 1
#3
#1 2 3

#Sample output:
#Case #1: 4
#Case #2: 1
#Case #3: 2
#Case #4: 0


import sys

def findOps(num, prev):
  ops = 0
  while num <= prev:
    if ops > 0 and (num + (10 ** ops-1)) > prev:
      num = prev+1
    else:
      num = num*10
      ops += 1
  return num, ops

def appendSort(elements, inputList):
    ops = 0
    prev = inputList[0]
    l = len(inputList)
    for idx in range(1, l):
      num = inputList[idx]
      if num <= prev:
        num, op = findOps(num, prev)
        ops += op
      prev = num
    return ops

tests = int(sys.stdin.readline())
for i in range(1, tests + 1):
    elements, inputList = int(sys.stdin.readline()), sys.stdin.readline().split()
    inputList = [int(x) for x in inputList]
    cost = appendSort(elements, inputList)
    print("Case #"+str(i)+":", cost)
