def sumpossible(b,n, num):
    t=[[False for i in range(num+1)] for j in range((n+1))]
    
    for i in range (n+1):
        t[i][0]=True
    for i in range(1, num+1):
        t[0][i]=False
    for i in range(1,n+1):
        for j in range(1, num+1):
            if j< t[i-1]:
                t[i][j]=t[i-1][j]
            if j>=t[i-1]:
                t[i][j]=(t[i-1][j] or t[i-1][j-t[i-1]])

    return t[n][num]

#nu=int(input())
#arr=list(map(int, input().split()))
#a=list(map(int,input().split()))
#n2=int(input())
nu=2
arr=[3,2]
n2=4
z=[3,8,11,13]
print(n2)
#z=list(map(int,input().split()))

b=[]
for i in range(nu):
    sumi=0
    for j in range(i+1):
        sumi=sumi+(arr[j]* 2**j)
		b.append(sumi)
print(b)

out=[]
'''
for i in z:
    if sumpossible(b,len(b),i):
        out.append("YES")
    else:
        out.append("NO")
st=" ".join(out)
print("{}".format(st))
'''