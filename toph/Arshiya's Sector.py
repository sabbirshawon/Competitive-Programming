import math
n = int(input())
for i in range(n):
  r,a=list(map(int,input().split()))
  area = (math.pi*r*r)*(a/360)
  print (area)
	
#sabbirs
