n=int(input())
for i in range(n):
  a,b,c = map(int,input().split())
  if a>b and a>c:
    print("Case {}: {}".format(i+1,"A"))
  elif b>a and b>c:
    print("Case {}: {}".format(i+1,"B"))
  elif c>a and c>b:
    print("Case {}: {}".format(i+1,"C"))
  else:
    print("Case {}: {}".format(i+1,"Confused"))
	
#sabbirs
