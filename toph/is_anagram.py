a = input()
b = input()
def anagram(a,b):
    l1=list(a)
    l2=list(b)
    if sorted(l1) == sorted(l2):
        print("Yes")
    else:
        print("No")
anagram(a,b)
