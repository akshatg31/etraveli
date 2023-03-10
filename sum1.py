arr=[1,3,5]
m=len(arr)
N=int(input())
cnt=0
for i in range(m-1):
    for j in range(i,m):
        if((arr[i]+arr[j]==N)):
            cnt+=1
        elif(abs(arr[i]-arr[j]==N)):
            cnt+=1
print(cnt)