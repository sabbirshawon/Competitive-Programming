import math
f=math.factorial
n=int(input())
for i in range(n):
    x,y = str(input()).split()
    x,y = int(x), int(y)
    if y>=x:
        print(0)
    else:
        print(int(f(x-1)/f(y)/f(x-1-y)))	
        
#Author : Sabbir Ahmed
#Author URL: https://toph.co/u/Sabbirs
#Github Pages: http://sabbirshawon.github.io/