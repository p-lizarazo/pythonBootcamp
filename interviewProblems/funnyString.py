#determine wether a a string is funny or # NOTE:
n = int(input(""))
while(n):
    s = input("")
    isTrue=True
    for i in range(len(s)):
        if(i==len(s)-1):
            break
        r1 = abs(ord(s[i])-ord(s[i+1]))
        r2 = abs(ord(s[-i-1])-ord(s[-i-2]))
        if(r2!=r1):
            isTrue=False
            break

    if(isTrue):
        print("Funny")
    else:
        print("Not Funny")
    n-=1
