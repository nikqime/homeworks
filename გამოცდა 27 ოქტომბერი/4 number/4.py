#   4) Factorial Calculation (3 ქულა)
#      Create a program that receives a non-negative integer and returns its factorial. The factorial of a number n is the product of all positive #      integers from 1 to n. By definition, the factorial of 0 is 1.
#      Examples:
#      5 --> 120
#      0 --> 1
def factorial(x):
    res=1
    n=x
    while n>0:
        res *= n
        n-=1
    return res
number=9
new_number=factorial(number)
print(new_number)
        

    