
s=input()
d1 = {}
l=[]
str=""

def func1(nList,resp,indice):
    if(sum(i for _, i in nList)>len(str)):
        return None
    if(not nList):
        return resp
    if(not str):
        return None

    for i,e in enumerate(nList):
        index = str.find(e[0],indice,len(str))
        if(index==-1):
            return None

        tempList = []
        for c,n in nList:
            tempList.append([c,n])

        tempList[i][1]-=1
        if(tempList[i][1]==0):
            del tempList[i]
        re=func1(tempList,resp+e[0],index+1)
        if(re!=None):
            return re

for c in s:
    try:
        d1[c]+=1
    except:
        d1[c]=1

for k,v in d1.items():
    l.append([k,int(v/2)])
l= sorted(l,reverse=False)
str = s[::-1]
r=func1(l,"",0)

print(r)
