#sum of digits and number of digits

print("Enter the number")
num = int(input())
temp = num
sum = 0
cnt = 0
while temp != 0:
    sum += temp%10
    temp = temp//10
    cnt += 1
print("Sum of the digits of", num,"=",sum)
print("Number of digits in",num,"=",cnt)