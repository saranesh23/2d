t=list(map(str,input().split()))
s=0
for i in range(0,len(t)):
    k=t[i]
    a=k[::-1]
    if k==a:
        s+=1
    
print(s)    

