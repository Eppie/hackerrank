n,k,q=map(int,input().split())
a=list(map(int,input().split()))
exec("a.insert(0,a.pop());"*k)
exec("print(a[int(input())]);"*q)
