import math
n = int(input())
for i in range(n):
  r,a=list(map(int,input().split()))
  area = (math.pi*r*r)*(a/360)
  print (area)
	
#Author : Sabbir Ahmed
#Author URL: https://toph.co/u/Sabbirs
#Github Pages: http://sabbirshawon.github.io/
