q = int(input())
dict = {}
dict1 = {}
l = []

def query(type,value):
    if(type==1):
        if(dict.get(value)!=None):
            dict1[dict[value] ] -=1
            dict[value]+=1
            if(dict1.get(dict[value])!=None):
                dict1[dict[value]] +=1
            else:
                dict1[dict[value]] =1
        else:
            dict[value]=1
            if(dict1.get(dict[value])!=None):
                dict1[dict[value]]+=1
            else:
                dict1[dict[value]]=1

    elif(type==2):
        if(dict.get(value)!=None):
            if(dict[value]>0):
                dict1[dict[value]]-=1
                dict1[dict[value]-1]+=1
                dict[value]-=1

    elif(type==3):
        if(dict1.get(value)!=None):
            if(dict1[value]>0):
                l.append(1)
            else:
                l.append(0)
        else:
            l.append(0)

dict1[0]=0 #Just an inittial condition to avoid KeyError
for _ in range(q):
    a,b=list( map(int,input().split()) )
    query(a,b)
print('\n'.join(map(str, l)))
