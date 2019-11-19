t = int(input())
for i in range(1,t+1,1):
	l,w,d = map(float,input().split())
	area = ((w*l)-(d*l))/2
	print("Case",str(i)+":","%.2f" % area)

	
#Author : Sabbir Ahmed
#Author URL: https://toph.co/u/Sabbirs
#Github Pages: http://sabbirshawon.github.io/