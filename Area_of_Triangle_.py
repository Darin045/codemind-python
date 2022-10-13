a,b,c=map(int,input().split())
s=(a+b+c)/2
t=s*(s-a)*(s-b)*(s-c)
h=t**0.5
print("{:.2f}".format(h))