#strong number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("Enter the number")
num = int(input())
temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum += factorial(digit)
    num = num // 10

if sum == temp:
    print(temp, "is a strong number")
else:
    print(temp, "is not a strong number")
