#Left rotation

n,d = map(int,input().split() )
l = input().split()
residual = d%n
s = ""
for i in range(len(l)):
    s += (l[(i+residual) % n]) + " "
print(s)
