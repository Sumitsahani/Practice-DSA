# Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.

# Example 1:
# Input: N = 6, array[] = {13,46,24,52,20,9}
# Output: 9,13,20,24,46,52
# Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52

# Example 2:
# Input: N=5, array[] = {5,4,3,2,1}
# Output: 1,2,3,4,5
# Explanation: After sorting the array is: 1, 2, 3, 4, 5


n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    minIdx = i
    for j in range(i + 1, n):
        if arr[minIdx] > arr[j]:
            minIdx = j
    temp = arr[minIdx]
    arr[minIdx] = arr[i]
    arr[i] = temp

print(*arr)
