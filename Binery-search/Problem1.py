# Question: find x is greater then and equal to k?
n=int(input())
arr=list(map(int,input().split()))
k=int(input()) 

low=0
high=n-1
ans=n #default
def check(mid):
    if arr[mid]>=k:
        return 1
    else:
        return 0
    
while(low<=high):
    mid=low+(high-low)//2
    if(check(mid)==1):
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)
