low = 0
high = 1000000

for i in range(1,26):
    mid = (low + high) // 2
    print(mid)
    ans = input()
    if ans == "Bigger":
        low = mid + 1
    elif ans == "Smaller":
        high = mid - 1
    else:
        break
	
#Author : Sabbir Ahmed
#Author URL: https://toph.co/u/Sabbirs
#Github Pages: http://sabbirshawon.github.io/
