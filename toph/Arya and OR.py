t = int(input())
for i in range(t):
	input()
	n=list(map(int,input().split()))
	a=n[0]
	for j in n:a|=j
	print("Case {}: {}".format(i+1,a))



#Author : Sabbir Ahmed
#Author URL: https://toph.co/u/Sabbirs
#Github Pages: http://sabbirshawon.github.io/