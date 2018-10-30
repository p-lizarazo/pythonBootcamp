q = int(input())
d1 = {}
d2 = {}
l = []

def query(type,value):
    if(type==1):
        if(d1.get(value)!=None):
            d2[d1[value] ] -=1
            d1[value]+=1
            if(d2.get(d1[value])!=None):
                d2[d1[value]] +=1
            else:
                d2[d1[value]] =1
        else:
            d1[value]=1
            if(d2.get(d1[value])!=None):
                d2[d1[value]]+=1
            else:
                d2[d1[value]]=1

    elif(type==2):
        if(d1.get(value)!=None):
            if(d1[value]>0):
                d2[d1[value]]-=1
                d2[d1[value]-1]+=1
                d1[value]-=1

    elif(type==3):
        if(d2.get(value)!=None):
            if(d2[value]>0):
                l.append(1)
            else:
                l.append(0)
        else:
            l.append(0)

d2[0]=0 #Just an inittial condition to avoid KeyError
for _ in range(q):
    a,b=list( map(int,input().split()) )
    query(a,b)
print('\n'.join(map(str, l)))
