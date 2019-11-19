n = int(input())
for i in range(n):
  a,b = list(map(int,input().split()))
  add = a+b
  avg = add//2
  if(avg%2==0):
    print("Sadia will be happy.")
  else:
    print("Oops!")
	
#Author : Sabbir Ahmed
#Author URL: https://toph.co/u/Sabbirs
#Github Pages: http://sabbirshawon.github.io/
