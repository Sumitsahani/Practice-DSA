# Question 2 Rotated Array
# Given a rotated sorted array. Find the index of the minimum element in the array.

# All the elements are distinct.

n=int(input())
arr=list(map(int, input().split()))


low=0
high=n-1
ans=0 #default

def check(mid):
    if arr[mid]<arr[0]:
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