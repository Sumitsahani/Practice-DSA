n=int(input())
arr=list(map(int,input().split()))
flag=True
for i in range(n-1):
     for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(*arr)



