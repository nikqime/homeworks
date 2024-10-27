#7) Fibonacci Sequence Generator (4 ქულა)
#Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each #subsequent number is the sum of the previous two.
#Examples:

def pabrika(x):
    start=[0,1]
    while len(start)<x:
        start.append(start[-1]+start[-2])
    return start[:x]
print(pabrika(7))