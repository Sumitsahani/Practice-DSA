# Problem Statement: Given an integer N, return the number of digits in N.

# Examples
# Example 1:
# Input:N = 12345
# Output:5
# Explanation:  The number 12345 has 5 digits.
# Example 2:
# Input:N = 7789
# Output: 4
# Explanation: The number 7789 has 4 digits.

n =int(input())
count = 0
while n != 0:
    count += 1
    n = n // 10
print(count)