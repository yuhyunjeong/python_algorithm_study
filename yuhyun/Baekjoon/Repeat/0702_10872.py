import math
import sys


num = int(sys.stdin.readline())

result=1
for i in range(1,num+1) :
    result *= i

print(result)

"""num = int(input())

print(math.factorial(num))    """