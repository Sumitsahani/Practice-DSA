# Question 3: Finding Peak element  
n= int(input())
arr=list(map(int,input().split()))

low =0
high =n-1
ans=-1
def check(mid):
    if arr[mid]>arr[mid+1]:
        return 1
    else:
        return 0
while(low<=high):
    mid=low+(high-low)//2
    if check(mid)==1:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(arr[ans])