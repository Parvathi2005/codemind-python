a,b,c=map(int,input().split())
S=(a+b+c)/2
T=(S*(S-a)*(S-b)*(S-c))**0.5
print("%0.2f"%T)