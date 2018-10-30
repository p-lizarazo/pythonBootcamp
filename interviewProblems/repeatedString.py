s = input()
n = int(input())

residual = n%len(s)
times = int(n/len(s))

a=s[:residual].count("a")
b=s[residual:].count("a")

print( (a+b)*times+a )
